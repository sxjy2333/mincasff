import os
import urllib.request


def get_local_version():
    if os.path.exists("version.txt"):
        with open("version.txt", "r") as file:
            return file.read().strip()
    return None


def get_remote_version(remote_url):
    try:
        response = urllib.request.urlopen(remote_url)
        return response.read().decode("utf-8").strip()
    except Exception as e:
        print("无法获取远程版本:", str(e))
        return None


def download_update(update_url):
    try:
        os.system("start " + update_url)
    except Exception as e:
        print("无法打开更新文件:", str(e))


def main():
    local_version = get_local_version()
    if local_version is None:
        print("本地版本文件不存在或无法读取")
        return

    remote_version = get_remote_version("https://c.mhkvm.com/potpvp/version.txt")
    if remote_version is None:
        print("无法获取远程版本信息")
        return

    print("本地版本:", local_version)
    print("远程版本:", remote_version)

    if local_version < remote_version:
        print("该版本需要更新")
        print("点击这个链接进行更新：https://kook.top/UYIjlV")
    else:
        print("已经是最新版本")
        print("放心游玩哦~")


remote_url = "https://c.mhkvm.com/potpvp/mess.txt"
try:
    response = urllib.request.urlopen(remote_url)
    content = response.read().decode("utf-8")
    print("更新内容:")
    print(content)
except Exception as e:
    print("无法获取远程文件内容:", str(e))

if __name__ == "__main__":
    main()

input("Please Input Any Key To Exit!")
