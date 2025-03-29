import requests
import asyncio
import time
import json
from douyin_const import ua

"""
 获取抖音榜单数据
"""
async def get_douyin_music():
    """
    获取抖音Top50音乐榜单
    :return:
    """
    url = f"https://api3-normal-c-hl.amemv.com/aweme/v1/chart/music/list/?request_tag_from=rn&chart_id=6853972723954146568" \
          f"&count=100&cursor=0&os_api=22&device_type=MI 9" \
          f"&ssmix=a&manifest_version_code=110101&dpi=240&uuid=262324373952550&app_name=aweme&version_name=11.1.0&ts={round(time.time())}" \
          f"&cpu_support64=false&app_type=normal&ac=wifi&host_abi=armeabi-v7a&update_version_code" \
          f"=11109900&channel=douyinw&_rticket={round(time.time() * 1000)}&device_platform=android&iid=157935741181076" \
          f"&version_code=110100&cdid=02a0dd0b-7ed3-4bb4-9238-21b38ee513b2&openudid=af450515be7790d1&device_id=3166182763934663" \
          f"&resolution=720*1280&os_version=5.1.1&language=zh&device_brand=Xiaomi&aid=1128&mcc_mnc=46007"

    res = requests.get(url, headers={"User-Agent": ua["app"]}).json()
    for i in range(0, len(res["music_list"]) - 1):
        music_item = res["music_list"][i]
        # print("music_id:", music_item)
        print(json.dumps(music_item, indent=4, ensure_ascii=False))


if __name__ == '__main__':
     asyncio.run(get_douyin_music())

