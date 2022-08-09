import time
import pyautogui
import cv2
import audioop
import pyaudio
import wave
count = 0
# 使用前请将系统默认录制设备改成“立体声混音”，否则无法录音
'''
1.点击“原文播放”
2.开始录音
3.停止录音
4.点击“开始录音”
5.播放录音
6.播放完之后点击“停止录音”
'''
def get_xy(img_model_path):
    """
    获取点击目标的坐标中心
    :param img_model_path:指定点击目标的模板
    :return: 指定点击目标的坐标中心
    """
    # 将图片截图并且保存
    pyautogui.screenshot().save("./pic/screenshot.png")
    # 待读取图像
    img = cv2.imread("./pic/screenshot.png")
    # 图像模板
    img_t = cv2.imread(img_model_path)
    # 读取模板的高度宽度和通道数
    height, width, channel = img_t.shape
    # 使用matchTemplate进行模板匹配（标准平方差匹配）
    result = cv2.matchTemplate(img, img_t, cv2.TM_SQDIFF_NORMED)
    # 解析出匹配区域的左上角图标
    upper_left = cv2.minMaxLoc(result)[2]
    # 计算出匹配区域右下角图标（左上角坐标加上模板的长宽即可得到）
    lower_right = (upper_left[0] + width, upper_left[1] + height)
    # 计算坐标的平均值并将其返回
    avg = (int((upper_left[0] + lower_right[0]) / 2), int((upper_left[1] + lower_right[1]) / 2))
    return avg


def auto_Click(var_avg):
    """
    输入一个元组，自动点击
    :param var_avg: 坐标元组
    :return: None
    """
    pyautogui.click(var_avg[0], var_avg[1], button='left')
    time.sleep(1)


def routine(img_model_path, name):
    """
    输入点击目标的模板，自动点击
    :param img_model_path:图像模板
    :return: None
    """
    avg = get_xy(img_model_path)  # 获取点击目标的坐标中心
    print(f"正在点击{name}")
    auto_Click(avg)  # 点击目标


def record():
    # 录音
    pa = pyaudio.PyAudio()
    stream = pa.open(format=pyaudio.paInt16, channels=2, rate=16000, input=True, frames_per_buffer=2048)  # 初始化录音
    record_buf = []  # 新建存放录音二进制数据的列表
    while True:
        audio_data = stream.read(2048)  # 读出声卡缓冲区的音频数据
        record_buf.append(audio_data)  # 将读出的音频数据追加到record_buf列表
        volume = (audioop.rms(audio_data, 2))  # 实时监测播放录音的音量
        print('录音中',volume)
        if volume <= 2:  # 在我电脑上没有声音时检测的音量就是2
            count += 1
        else:            # 如果连续20次采样都没有音量就判定录音已经播完，结束录音
            count = 0
        if count == 20:
            break

    if record_buf != 0:  # 防止写入空文件
        wf = wave.open('./pic/01.wav', 'wb')  # 创建一个音频文件，名字为“01.wav"
        wf.setnchannels(2)  # 设置声道数为2
        wf.setsampwidth(2)  # 设置采样深度为
        wf.setframerate(16000)  # 设置采样率为16000
        # 将数据写入创建的音频文件
        wf.writeframes("".encode().join(record_buf))
        # 写完后将文件关闭
        wf.close()
        # 停止声卡
        stream.stop_stream()
        # 关闭声卡
        stream.close()
        # 终止pyaudio
        pa.terminate()
def play():
    # 播放刚刚的录音
    chunk = 1024
    wf = wave.open(r"./pic/01.wav", 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), channels=wf.getnchannels(),
                    rate=wf.getframerate(), output=True)

    data = wf.readframes(chunk)  # 读取数据

    while len(data) != 0:  # 把整个文件播完
        stream.write(data)
        data = wf.readframes(chunk)
        print('播放中')

    stream.stop_stream()  # 停止数据流
    stream.close()
    p.terminate()  # 关闭 PyAudio
    print('结束播放！')



routine("./pic/yuan.png", "播放")
record()
routine("./pic/luyin.png", "录音")
play()
routine("./pic/stop.png", "停止")

'''
这个项目是无聊时做的，禁止商用
本项目遵守 GPL v3开源协议
'''