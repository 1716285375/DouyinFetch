import pprint
import re
from typing import Any
from httpx import AsyncClient
import asyncio


async def get_sec_uid(room_id: str) -> str:
    headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
    }
    cookies = {
        "__ac_nonce": "0678a618700d5394bd29"
    }
    url = f'https://live.douyin.com/{room_id}'
    # 获取html数据
    async with AsyncClient(default_encoding='utf-8') as client:
        response = await client.get(url, headers=headers, cookies=cookies)
        response.raise_for_status()
        # 响应状态
        if response.status_code == 200:
            res = response.text
            # >>> 获取直播房间信息
            room_id = re.findall(r'\\"roomId\\":\\"(\d+)\\"', res)[0]
            print(room_id)
            sec_uid = re.search(r'\\"sec_uid\\":\\"([^"]+)\\"', res).group(1)
            if sec_uid:
                return sec_uid
            else:
                return ''
        else:
            return ''


async def get_user_info(sec_uid: str) -> dict[str, Any] | None:
    """
    获取抖音账户主页信息
    :param name:
    :return:
    """
    cookies = {
        'enter_pc_once': '1',
        'UIFID_TEMP': '8f584679f13361d7674396b25a46f1c75dd7736730eef2bca7f1b3cfea8b216d37fa41e7b31e63c33278c49489e96bce795cb9e4ba1e4bcb9d57659d2a1c675d37736db22a9a7775bdc7aa281128341d',
        'fpk1': 'U2FsdGVkX1+yrmPOXAfoG4AKNOufxjd7gJX+WqQ1pwTaSPLdzDW+GMdwNxl4e7tz4s9ZNW/fgFVPw/pxcK4FRg==',
        'fpk2': '8cf04e281318af421dc03fc482e00bfd',
        's_v_web_id': 'verify_mc9zww70_nB5YT3Pd_kzgK_4gJm_A7rz_L3USUvq3bFJK',
        'passport_csrf_token': 'ad4198855f86ed0aea8427cec3a613e9',
        'passport_csrf_token_default': 'ad4198855f86ed0aea8427cec3a613e9',
        '__security_mc_1_s_sdk_crypt_sdk': '892a2814-4936-a7e5',
        'bd_ticket_guard_client_web_domain': '2',
        'passport_assist_user': 'CkEufsZ6gyi_G0hc8FkdDPemPnlG_o9x-GGakYPIX7pHUpuOGVGKHwaAh4beImI5iBQ0j_qhF_QWUpLLblslm3baRRpKCjwAAAAAAAAAAAAATyeQBNk8JTaaVX5AInvu1lituAdQkLgy0Np7s5Kld08DwAT2wLMwD6ozEYHvqRPbhOgQxvj0DRiJr9ZUIAEiAQNFbKmr',
        'n_mh': 'YSNL1hOjnfMIVJkyp0jrZ4l_hUDn-0kBXL6ZkFFP1Y0',
        'uid_tt': '8603298cf76c617c83f63c17db829c3f',
        'uid_tt_ss': '8603298cf76c617c83f63c17db829c3f',
        'sid_tt': 'c03386c94d42f4445b30e0f0858b834a',
        'sessionid': 'c03386c94d42f4445b30e0f0858b834a',
        'sessionid_ss': 'c03386c94d42f4445b30e0f0858b834a',
        'session_tlb_tag': 'sttt%7C13%7CwDOGyU1C9ERbMODwhYuDSv_________I3RglQDkZejOL4kHu7XWfHgA0o-08eUwjeu-v1dO-EiE%3D',
        'is_staff_user': 'false',
        'login_time': '1750737533346',
        'UIFID': '8f584679f13361d7674396b25a46f1c75dd7736730eef2bca7f1b3cfea8b216d37fa41e7b31e63c33278c49489e96bce4e8ccd0574fb78b0fc230ddc8de9b1679df2e4989a9aa1de8c39ec81572a6c8a855f02f27740f808be17266eb72fb776ea42e0ac9cb8bae62941bebd5354161cefbcdc09a9d6b467d34a60e3bfb73d52a9ec710ca2befacfc9a79d0438dfbddc4c9e2462a436659ce1bc02e39ff0aede',
        'SelfTabRedDotControl': '%5B%5D',
        '_bd_ticket_crypt_cookie': '63b0eff7829e9cfbd7ef661e302f4854',
        '__security_mc_1_s_sdk_sign_data_key_web_protect': '3daae32d-4c48-9268',
        '__security_mc_1_s_sdk_cert_key': 'da9d82ee-420b-9642',
        '__security_server_data_status': '1',
        'live_use_vvc': '%22false%22',
        'SEARCH_RESULT_LIST_TYPE': '%22single%22',
        'my_rd': '2',
        'xgplayer_device_id': '1258076974',
        'xgplayer_user_id': '155763425833',
        'passport_auth_status': '98c50b2037d7caffbeec2b5c4a34bf97%2C6be271e8eb7c296177496693b041da53',
        'passport_auth_status_ss': '98c50b2037d7caffbeec2b5c4a34bf97%2C6be271e8eb7c296177496693b041da53',
        'passport_mfa_token': 'Cjf4O9YcSp0uUAEU49xjOIJwJqMu8kdBLh9SYvcWYh%2F9c%2FPW2Cn7B71Cp8SBAzRE0QEcbn89gTyrGkoKPAAAAAAAAAAAAABPLAqNpPQvXAkHiFbLAjT%2B4pLJHDshq0VuIgA5bEkGjBTZA%2BG6uZa3CqDzdE5H3sypiBCMtPUNGPax0WwgAiIBA4zXhWc%3D',
        'd_ticket': '0dfd6fd86c8b973f664c0bd8ef23a71729e79',
        'hevc_supported': 'true',
        'sid_guard': 'c03386c94d42f4445b30e0f0858b834a%7C1752844268%7C5184000%7CTue%2C+16-Sep-2025+13%3A11%3A08+GMT',
        'sid_ucp_v1': '1.0.0-KDRiM2UwMzc3MmEyYjAyMWI0YWU2NWI4ZTM4NmY2YTdiMmI2NTQ1Y2IKIQietuDhh_SrAxDsj-nDBhjvMSAMMKWHn_gFOAJA8QdIBBoCaGwiIGMwMzM4NmM5NGQ0MmY0NDQ1YjMwZTBmMDg1OGI4MzRh',
        'ssid_ucp_v1': '1.0.0-KDRiM2UwMzc3MmEyYjAyMWI0YWU2NWI4ZTM4NmY2YTdiMmI2NTQ1Y2IKIQietuDhh_SrAxDsj-nDBhjvMSAMMKWHn_gFOAJA8QdIBBoCaGwiIGMwMzM4NmM5NGQ0MmY0NDQ1YjMwZTBmMDg1OGI4MzRh',
        '__live_version__': '%221.1.3.6301%22',
        'live_can_add_dy_2_desktop': '%221%22',
        'download_guide': '%220%2F%2F1%22',
        'publish_badge_show_info': '%221%2C0%2C0%2C1753454354334%22',
        'FOLLOW_LIVE_POINT_INFO': '%22MS4wLjABAAAANs9j26y951mf_R9IJttcOgRL4H0HIG1Ey2XbWliSHuJKERrlwU1IJ8k5TxVNWwYP%2F1753459200000%2F0%2F1753454361068%2F0%22',
        'is_dash_user': '1',
        'volume_info': '%7B%22isUserMute%22%3Atrue%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.379%7D',
        'playRecommendGuideTagCount': '1',
        'totalRecommendGuideTagCount': '1',
        'dy_swidth': '1920',
        'dy_sheight': '1080',
        'strategyABtestKey': '%221753787319.082%22',
        'WallpaperGuide': '%7B%22showTime%22%3A0%2C%22closeTime%22%3A0%2C%22showCount%22%3A0%2C%22cursor1%22%3A17%2C%22cursor2%22%3A4%7D',
        '__ac_nonce': '06888b49e00537f27c279',
        '__ac_signature': '_02B4Z6wo00f01LlVsXQAAIDDJzER5CtAbHS5dbXAAEbi65',
        'bd_ticket_guard_client_data': 'eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCRHJFYWs2eU5OK1gxeGo0SUh3bXdienJEM1RHaEhvZmh0d2NoS3RicUdUTmNTZW1tZllXRGpJcHNWVUxZSktVbEJjSUhSZHU5aGlOeVk3OTU0QmZZL0E9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D',
        'FOLLOW_NUMBER_YELLOW_POINT_INFO': '%22MS4wLjABAAAANs9j26y951mf_R9IJttcOgRL4H0HIG1Ey2XbWliSHuJKERrlwU1IJ8k5TxVNWwYP%2F1753804800000%2F0%2F0%2F1753790953480%22',
        'odin_tt': 'fa5ec5863010002f512e2cd6423187f20181ce9cdda90217a16cc6e54e144d2ebebd40e4f60fd0fa454a57a717cee0cfd0d1e8868e4ed8c699e92ad2b5442d7d',
        'biz_trace_id': 'b87ad136',
        'ttwid': '1%7CVvT-aCVd-jQr7wocfY2NpH1_BMJqm7HpOcAMfPTyUCM%7C1753789757%7Ce59c069d3370e4f487f7906e200ae0281bfb0016cf0ef7520a8c6438f0fa47a1',
        'passport_fe_beating_status': 'false',
        'IsDouyinActive': 'true',
        'home_can_add_dy_2_desktop': '%220%22',
        'stream_recommend_feed_params': '%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1920%2C%5C%22screen_height%5C%22%3A1080%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A20%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A100%7D%22',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'priority': 'u=1, i',
        'referer': f'https://www.douyin.com/user/{name}',
        'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        # 'uifid': '8f584679f13361d7674396b25a46f1c75dd7736730eef2bca7f1b3cfea8b216d37fa41e7b31e63c33278c49489e96bce4e8ccd0574fb78b0fc230ddc8de9b1679df2e4989a9aa1de8c39ec81572a6c8a855f02f27740f808be17266eb72fb776ea42e0ac9cb8bae62941bebd5354161cefbcdc09a9d6b467d34a60e3bfb73d52a9ec710ca2befacfc9a79d0438dfbddc4c9e2462a436659ce1bc02e39ff0aede',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
        # 'cookie': 'enter_pc_once=1; UIFID_TEMP=8f584679f13361d7674396b25a46f1c75dd7736730eef2bca7f1b3cfea8b216d37fa41e7b31e63c33278c49489e96bce795cb9e4ba1e4bcb9d57659d2a1c675d37736db22a9a7775bdc7aa281128341d; fpk1=U2FsdGVkX1+yrmPOXAfoG4AKNOufxjd7gJX+WqQ1pwTaSPLdzDW+GMdwNxl4e7tz4s9ZNW/fgFVPw/pxcK4FRg==; fpk2=8cf04e281318af421dc03fc482e00bfd; s_v_web_id=verify_mc9zww70_nB5YT3Pd_kzgK_4gJm_A7rz_L3USUvq3bFJK; passport_csrf_token=ad4198855f86ed0aea8427cec3a613e9; passport_csrf_token_default=ad4198855f86ed0aea8427cec3a613e9; __security_mc_1_s_sdk_crypt_sdk=892a2814-4936-a7e5; bd_ticket_guard_client_web_domain=2; passport_assist_user=CkEufsZ6gyi_G0hc8FkdDPemPnlG_o9x-GGakYPIX7pHUpuOGVGKHwaAh4beImI5iBQ0j_qhF_QWUpLLblslm3baRRpKCjwAAAAAAAAAAAAATyeQBNk8JTaaVX5AInvu1lituAdQkLgy0Np7s5Kld08DwAT2wLMwD6ozEYHvqRPbhOgQxvj0DRiJr9ZUIAEiAQNFbKmr; n_mh=YSNL1hOjnfMIVJkyp0jrZ4l_hUDn-0kBXL6ZkFFP1Y0; uid_tt=8603298cf76c617c83f63c17db829c3f; uid_tt_ss=8603298cf76c617c83f63c17db829c3f; sid_tt=c03386c94d42f4445b30e0f0858b834a; sessionid=c03386c94d42f4445b30e0f0858b834a; sessionid_ss=c03386c94d42f4445b30e0f0858b834a; session_tlb_tag=sttt%7C13%7CwDOGyU1C9ERbMODwhYuDSv_________I3RglQDkZejOL4kHu7XWfHgA0o-08eUwjeu-v1dO-EiE%3D; is_staff_user=false; login_time=1750737533346; UIFID=8f584679f13361d7674396b25a46f1c75dd7736730eef2bca7f1b3cfea8b216d37fa41e7b31e63c33278c49489e96bce4e8ccd0574fb78b0fc230ddc8de9b1679df2e4989a9aa1de8c39ec81572a6c8a855f02f27740f808be17266eb72fb776ea42e0ac9cb8bae62941bebd5354161cefbcdc09a9d6b467d34a60e3bfb73d52a9ec710ca2befacfc9a79d0438dfbddc4c9e2462a436659ce1bc02e39ff0aede; SelfTabRedDotControl=%5B%5D; _bd_ticket_crypt_cookie=63b0eff7829e9cfbd7ef661e302f4854; __security_mc_1_s_sdk_sign_data_key_web_protect=3daae32d-4c48-9268; __security_mc_1_s_sdk_cert_key=da9d82ee-420b-9642; __security_server_data_status=1; live_use_vvc=%22false%22; SEARCH_RESULT_LIST_TYPE=%22single%22; my_rd=2; xgplayer_device_id=1258076974; xgplayer_user_id=155763425833; passport_auth_status=98c50b2037d7caffbeec2b5c4a34bf97%2C6be271e8eb7c296177496693b041da53; passport_auth_status_ss=98c50b2037d7caffbeec2b5c4a34bf97%2C6be271e8eb7c296177496693b041da53; passport_mfa_token=Cjf4O9YcSp0uUAEU49xjOIJwJqMu8kdBLh9SYvcWYh%2F9c%2FPW2Cn7B71Cp8SBAzRE0QEcbn89gTyrGkoKPAAAAAAAAAAAAABPLAqNpPQvXAkHiFbLAjT%2B4pLJHDshq0VuIgA5bEkGjBTZA%2BG6uZa3CqDzdE5H3sypiBCMtPUNGPax0WwgAiIBA4zXhWc%3D; d_ticket=0dfd6fd86c8b973f664c0bd8ef23a71729e79; hevc_supported=true; sid_guard=c03386c94d42f4445b30e0f0858b834a%7C1752844268%7C5184000%7CTue%2C+16-Sep-2025+13%3A11%3A08+GMT; sid_ucp_v1=1.0.0-KDRiM2UwMzc3MmEyYjAyMWI0YWU2NWI4ZTM4NmY2YTdiMmI2NTQ1Y2IKIQietuDhh_SrAxDsj-nDBhjvMSAMMKWHn_gFOAJA8QdIBBoCaGwiIGMwMzM4NmM5NGQ0MmY0NDQ1YjMwZTBmMDg1OGI4MzRh; ssid_ucp_v1=1.0.0-KDRiM2UwMzc3MmEyYjAyMWI0YWU2NWI4ZTM4NmY2YTdiMmI2NTQ1Y2IKIQietuDhh_SrAxDsj-nDBhjvMSAMMKWHn_gFOAJA8QdIBBoCaGwiIGMwMzM4NmM5NGQ0MmY0NDQ1YjMwZTBmMDg1OGI4MzRh; __live_version__=%221.1.3.6301%22; live_can_add_dy_2_desktop=%221%22; download_guide=%220%2F%2F1%22; publish_badge_show_info=%221%2C0%2C0%2C1753454354334%22; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAANs9j26y951mf_R9IJttcOgRL4H0HIG1Ey2XbWliSHuJKERrlwU1IJ8k5TxVNWwYP%2F1753459200000%2F0%2F1753454361068%2F0%22; is_dash_user=1; volume_info=%7B%22isUserMute%22%3Atrue%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.379%7D; playRecommendGuideTagCount=1; totalRecommendGuideTagCount=1; dy_swidth=1920; dy_sheight=1080; strategyABtestKey=%221753787319.082%22; WallpaperGuide=%7B%22showTime%22%3A0%2C%22closeTime%22%3A0%2C%22showCount%22%3A0%2C%22cursor1%22%3A17%2C%22cursor2%22%3A4%7D; __ac_nonce=06888b49e00537f27c279; __ac_signature=_02B4Z6wo00f01LlVsXQAAIDDJzER5CtAbHS5dbXAAEbi65; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCRHJFYWs2eU5OK1gxeGo0SUh3bXdienJEM1RHaEhvZmh0d2NoS3RicUdUTmNTZW1tZllXRGpJcHNWVUxZSktVbEJjSUhSZHU5aGlOeVk3OTU0QmZZL0E9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAANs9j26y951mf_R9IJttcOgRL4H0HIG1Ey2XbWliSHuJKERrlwU1IJ8k5TxVNWwYP%2F1753804800000%2F0%2F0%2F1753790953480%22; odin_tt=fa5ec5863010002f512e2cd6423187f20181ce9cdda90217a16cc6e54e144d2ebebd40e4f60fd0fa454a57a717cee0cfd0d1e8868e4ed8c699e92ad2b5442d7d; biz_trace_id=b87ad136; ttwid=1%7CVvT-aCVd-jQr7wocfY2NpH1_BMJqm7HpOcAMfPTyUCM%7C1753789757%7Ce59c069d3370e4f487f7906e200ae0281bfb0016cf0ef7520a8c6438f0fa47a1; passport_fe_beating_status=false; IsDouyinActive=true; home_can_add_dy_2_desktop=%220%22; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1920%2C%5C%22screen_height%5C%22%3A1080%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A20%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A100%7D%22',
    }
    params = {
        'device_platform': 'webapp',
        'aid': '6383',
        'channel': 'channel_pc_web',
        'publish_video_strategy_type': '2',
        'source': 'channel_pc_web',
        'sec_user_id': name,
        'personal_center_strategy': '1',
        'profile_other_record_enable': '1',
        'land_to': '1',
        'update_version_code': '170400',
        'pc_client_type': '1',
        'pc_libra_divert': 'Windows',
        'support_h265': '1',
        'support_dash': '1',
        'cpu_core_num': '20',
        'version_code': '170400',
        'version_name': '17.4.0',
        'cookie_enabled': 'true',
        'screen_width': '1920',
        'screen_height': '1080',
        'browser_language': 'zh-CN',
        'browser_platform': 'Win32',
        'browser_name': 'Edge',
        'browser_version': '138.0.0.0',
        'browser_online': 'true',
        'engine_name': 'Blink',
        'engine_version': '138.0.0.0',
        'os_name': 'Windows',
        'os_version': '10',
        'device_memory': '8',
        'platform': 'PC',
        'downlink': '10',
        'effective_type': '4g',
        'round_trip_time': '100',
        # 'webid': '7519360284424701452',
        # 'uifid': '8f584679f13361d7674396b25a46f1c75dd7736730eef2bca7f1b3cfea8b216d37fa41e7b31e63c33278c49489e96bce4e8ccd0574fb78b0fc230ddc8de9b1679df2e4989a9aa1de8c39ec81572a6c8a855f02f27740f808be17266eb72fb776ea42e0ac9cb8bae62941bebd5354161cefbcdc09a9d6b467d34a60e3bfb73d52a9ec710ca2befacfc9a79d0438dfbddc4c9e2462a436659ce1bc02e39ff0aede',
        # 'verifyFp': 'verify_mc9zww70_nB5YT3Pd_kzgK_4gJm_A7rz_L3USUvq3bFJK',
        'fp': 'verify_mc9zww70_nB5YT3Pd_kzgK_4gJm_A7rz_L3USUvq3bFJK',
        # 'msToken': 'sP1jrN_vD60cA9dlzQGbbksrPwIuGTr61tZOqhAKsD4QzQHKn6I5tKlwKVq9xBhDl9klYm0FSDHGPyQJQrEbWOM_p68pue3dhZxU2YwjWvFXkW1lfjD9lk0ptHbEuNj5EPeSZrsdhsCZt9CgW1TsVnDc8Hmd7IzjUHZ-QpALIhGJ7L-Kuv0x3AI=',
        # 'a_bogus': 'df45DeULEZ/VKdMbmKGA9GClUXElNBuyxaTObnZTyPzccqFT/uP9wrtqroz-4EAbPRphiC37ND0/bxxcTUUhZ9rpwmpDSKz6s02cVL8LhHHZTPJg7qDBeGtEFiPYUSsY8/AVi/WRUsMF2xQWIH9wABIHq/3nRREdFq3JVZYjT9u40WWjw929a3yQYX7qnf==',
    }

    async with AsyncClient() as client:
        response = await client.get(
            'https://www.douyin.com/aweme/v1/web/user/profile/other/',
            params = params,
            cookies = cookies,
            headers = headers,
        )
        response.raise_for_status()
        if response.status_code == 200:
            data = response.json()

            if data.get('status_msg') == 'UserId不合法':
                return None
            user = data.get('user')
            res = {
                'nickname': user.get('nickname'),
                'gender': user.get('gender'),
                'avatar_thumb': user.get('avatar_thumb'),
                'avatar_medium': user.get('avatar_medium'),
                'avatar_large': user.get('avatar_large'),
                'aweme_count': user.get('aweme_count'),
                'signature': user.get('signature'),
                'signature_language': user.get('signature_language'),
                'location': user.get('ip_location'),
                'follower_count': user.get('follower_count'),
                'max_follower_count': user.get('max_follower_count'),
                'molatform_followers_count': user.get('mplatform_followers_count'),
                'following_count': user.get('following_count'),
                'forward_count': user.get('forward_count'),
                'total_favorited': user.get('total_favorited'),
            }
            return res
        else:
            return None

async def main():
    # 测试
    # res = await get_user_info('MS4wLjABAAAACdtHOv8XS_X_PTuqJ3WReO4ka7pBWg7fmzG4wjiIZVkUKFOVtbhizl9GkpdOJ-O1')\
    res = await get_sec_uid('52466127183')
    pprint.pprint(res)

if __name__ == '__main__':
    asyncio.run(main())
