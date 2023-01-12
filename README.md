# 自动做E听说口语作业（仅限单词，发音，句子，课文跟读作业）
**使用前把系统默认录制设备调到立体声混音**

**推荐用pycharm,vscode等编辑器打开，方便修改参数**

**用pycharm打开，需要以管理员身份运行pycharm，不然无法正常点击**

这个项目不是很完善，对“逐句跟读”作业的适配不太好(main1.py)，甚至没有做GUI

还有增加了对配音的适配，但是因为配音的原文播放不是很清晰所以不太好用

### 环境依赖

Pyhton 3.1 （程序需要audioop库，python 3.11以上这个库就被弃用了）

Windows PC （e听说PC仅支持windows）
### 原理
通过opencv图像识别出“开始录音”“播放原文”等按键，然后点击播放，随即开始录音，实时监测音量，自动停止录音并播放，

**cycle(stop)函数的stop参数指的是停止录音的阈值，当连续(stop)次监测音量低于设定的值时。停止录音，因此参数越小反应越灵敏**

但stop参数过小容易误报，需要根据作业内容调节参数
### 需要的库
pyaudio

opencv

pyautogui

### 使用方法 
1.安装所需库（附一键安装脚本）

2.下载pic文件夹和main1.py（确保main1.py和pic文件夹在同一目录）

**3.调整第178行和第183行的cycle()函数的参数：读单词为10，读句子20-30，课文20-40**

3.打开e听说，开始做作业

4.确保E听说界面的“原文播放”,“下一个”和“开始录音”键不被挡住

5.启动**单词跟读.py**

### 常见问题

**Q1.为什么不会停止录音**

A:可能是没有切换成立体声混音

**Q2.鼠标移过去了，但是不点击**

A:要管理员身份运行

**Q3.误点击其他东西**

A.我才疏学浅，opencv玩的不是很明白，如果出现颜色，形状相似的，可能会误点，所以尽量不要出现颜色或图形相似的东西在屏幕上

**Q4.多显示器兼容吗**

A:没试过，不清楚pyautogui的机制，可能不行。还有如果是笔记本的话，不要用外接显示器，在我这里外接显示器会有识别bug

**Q5.Win7/8/11兼容吗**

A:没试过，理论上是兼容的，只要python版本在3.11以下

**Q9.为什么出现请正常朗读**

A：可能是音量太小，开启立体声混音后录音的音量会比你直接听到的小
