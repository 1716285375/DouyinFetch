# ------------------------------------------------------------
# -*- coding: utf-8 -*-
"""
@File           : main.py
@Author         : Jie
@CopyRight      : Copyright © 2025 Jie. All Rights Reserved
@Create Date    : 2025/7/29/21:18
@Update Date    :
@Description    : 
"""
# ------------------------------------------------------------

from fastapi import FastAPI
import uvicorn
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from info import get_user_info, get_sec_uid

app = FastAPI()


# 配置 CORS
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有 HTTP 方法
    allow_headers=["*"],  # 允许所有头部
)

@app.get("/user/{user_id}")
async def get_user_home_page_info(user_id: str):
    sec_uid_ = await get_sec_uid(user_id)
    user = await get_user_info(sec_uid_)
    # 返回 JSONResponse
    if user is not None:
        return JSONResponse(content=user, status_code=200)
    else:
        return JSONResponse(content={"error": "用户不存在或查询失败"}, status_code=404)



if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8848)