import json

zb_id = "33627"
cookie = json.loads(open("292070730.json", "r", encoding="utf-8").read())
system_version = "10.0.0"
app_v = "6270200"
app_innerver = "6.27.0"
phone = "HMA-AL00"


mozilla = f"Mozilla/5.0 (Linux; Android {system_version}; {phone} Build/{phone}; wv)"
app_le_web_kit = "AppleWebKit/537.36 (KHTML, like Gecko)"
version = "Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 os/android model/{phone}"
app_version = f"build/{app_v} osVer/{system_version} sdkInt/{29} network/2 BiliApp/{app_v}"
mobi_app = f"mobi_app/android channel/yingyongbao Buvid/{cookie['Buvid']} innerVer/{app_v}"
locale = f"c_locale/zh_CN s_locale/zh_CN 6.27.0 os/android model/{phone} mobi_app/android build/{app_v}"
channel = f"channel/yingyongbao innerVer/{app_v} osVer/{system_version} network/2"

mozilla_ = f"Mozilla/5.0 BiliDroid/{app_innerver} (bbcallen@gmail.com) os/android model/{phone}"
mobi_app_ = f"mobi_app/android build/{app_v} channel/yingyongbao innerVer/{app_v} osVer/{system_version} network/2"

user_agent_1 = f"{mozilla} {app_le_web_kit} {version} {app_version} {mobi_app} {locale} {channel}"
user_agent_2 = f"{mozilla_} {mobi_app_}"

header_1 = {
    "Accept-Encoding": "gzip",
    "User-Agent": user_agent_1,
    "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
    "native_api_from": "h5",
    "Referer": f"https://www.bilibili.com/h5/mall/suit/detail?id={zb_id}&navhide=1",
    "X-CSRF-TOKEN": str(cookie['bili_jct']),
    "Connection": "Keep-Alive",
    "Host": "api.bilibili.com"
}

header_2 = {
    "Accept-Encoding": "gzip",
    "User-Agent": user_agent_2,
    "Content-Type": "application/json",
    "APP-KEY": "android",
    "buildId": app_v,
    "Buvid": cookie['Buvid'],  # Buvid
    "Connection": "Keep-Alive",
    "Host": "pay.bilibili.com"
}


# print(header_1)
# print(header_2)
