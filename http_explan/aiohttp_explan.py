import aiohttp
import asyncio
from utils import timer


URLS = [
    'https://www.ccgp.gov.cn/cggg/dfgg/qtgg/202601/t20260129_26130057.htm',
    'https://www.ccgp.gov.cn/cggg/dfgg/cjgg/202601/t20260129_26130054.htm',
    'https://www.ccgp.gov.cn/cggg/dfgg/zbgg/202601/t20260129_26130049.htm'
]


async def fetch(session, url):
    """异步获取单个网页内容"""
    try:
        async with session.get(url) as response:
            # 只获取前100字符避免输出太长
            text = await response.text()
            print(f"✅ {url} | 状态: {response.status} | 内容长度: {len(text)}")
            return text

    except Exception as e:

        print(f"❌ 请求失败 {url}: {e}")
        return None


@timer
async def main():
    """主函数 并发请求所有URL"""
    async with aiohttp.ClientSession() as session:
        # 用create_task显示创建Task
        tasks = [asyncio.create_task(fetch(session, url)) for url in URLS]

        # 等待所有任务完成
        results = await asyncio.gather(*tasks)
        return results


asyncio.run(main())
