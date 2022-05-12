# minerProxyCrack

开源Python脚本，破解 @Char1esOrz 的minerProxy v3.0.3（以下简称303），修改作者抽水钱包为自己，有效防止 @Char1esOrz 暗抽，实现百分百收益

![avatar](https://i.postimg.cc/8zkc4Grz/Char1es-Orz.jpg)

## 目录

* [原理](https://github.com/minerproxycracked/minerProxyCrack#%E5%8E%9F%E7%90%86)
* [开始](https://github.com/minerproxycracked/minerProxyCrack#%E5%BC%80%E5%A7%8B)
* [注意](https://github.com/minerproxycracked/minerProxyCrack#%E6%B3%A8%E6%84%8F)
* [附录（内容供高级用户参考）](https://github.com/minerproxycracked/minerProxyCrack#%E9%99%84%E5%BD%95%E5%86%85%E5%AE%B9%E4%BE%9B%E9%AB%98%E7%BA%A7%E7%94%A8%E6%88%B7%E5%8F%82%E8%80%83)
* [备份](https://github.com/minerproxycracked/minerProxyCrack#%E5%A4%87%E4%BB%BD)
* [其它](https://github.com/minerproxycracked/minerProxyCrack#%E5%85%B6%E5%AE%83)

## 原理

303的各版本钱包地址信息如下

```
linux:

minerProxy/minerProxy_cmd:      大小8182977字节， 钱包地址位于0x0032780d
minerProxy_config:              大小8484988字节， 钱包地址位于0x0034d1cb
minerProxy_web:                 大小17611821字节，钱包地址位于0x00495638

windows:

minerProxy/minerProxy_cmd.exe:  大小8391168字节， 钱包地址位于0x0032a8ac
minerProxy_config.exe:          大小8757248字节， 钱包地址位于0x00357b1c
minerProxy_web.exe:             大小17880576字节，钱包地址位于0x004a07d5
```

由此均可得出@Char1esOrz的钱包为`46baD2c3b04A7A5cc055F1e8782782077DDaEb8B`，其E池挖矿地址为

https://ethermine.org/miners/46baD2c3b04A7A5cc055F1e8782782077DDaEb8B/dashboard

其它的盗版303均在上文相应地址信息处修改了作者抽水钱包，因此并无 @Char1esOrz 所说的暗抽100%，只是作者抽水变为盗版作者自己

例如，该典型的盗版303 https://github.com/minerproxyeth/minerproxy

根据上文相应地址信息不难得出其钱包为`E489845D5e4B38dF4639b2BC13f1F0C27B861f78`，其挖矿地址为

https://ethermine.org/miners/E489845D5e4B38dF4639b2BC13f1F0C27B861f78/dashboard

可以看到共同的`devfee303`矿工名。其余的盗版303还有很多，不一一列举

`crack303.py`将根据输入文件的**字节大小**判断是303的哪一个文件，进而根据地址信息进行修改

## 开始

### 1. 检查Python是否安装（Python2, Python3都可，若Python已安装则直接进入破解步骤）

对于linux/windows用户，输入`python --version`

若显示了Python的版本信息则说明已安装，若提示诸如`command not found`等则需安装

### 2. 安装Python

#### 2.1 linux

绝大多数linux系统自带Python2或Python3

若仍然没有版本信息

* ubuntu，debian用户：输入`sudo apt install python`
* centos用户：输入`yum install python`

待安装完成后，再输入`python --version`检查

#### 2.2 windows

在[Python官网](https://www.python.org/downloads/windows/)选择一个版本下载安装。安装时**需要**在安装程序底部勾选`Add Python 3.x to PATH`，否则需要自己配置PATH

确定安装好了后，输入`python --version`，显示Python的版本信息说明安装成功

### 3. 破解

#### 3.1 下载脚本

下载本仓库的Python脚本：https://github.com/minerproxycracked/minerProxyCrack/archive/refs/tags/v1.0.zip

对于linux用户，可使用`wget`命令下载

```
wget https://github.com/minerproxycracked/minerProxyCrack/archive/refs/tags/v1.0.zip
```

下载完毕后使用`unzip`命令解压到当前目录（注意不要忽略任何一个字符，包括最后那个点）

```
unzip v1.0.zip -d .
```

解压出的文件夹为`minerProxyCrack-1.0`，进入该目录

对于windows用户，下载、解压，进入解压的目录

#### 3.2 替换钱包（以下步骤linux和windows相同）

根据前文所述，`crack303.py`将根据输入文件的**字节大小**判断是303的哪一个文件，进而对钱包进行修改，因此文件大小需匹配303的任意一个版本

用法：`python crack303.py -t TARGET -w WALLET -o OUTPUT`

其中，`TARGET`为要破解的303文件，`WALLET`为要替换的钱包地址，`OUTPUT`为替换钱包后生成的文件

例如：将`minerProxy_web.exe`和`crack303.py`置于同一目录下，输入

```
python crack303.py -t minerProxy_web.exe -w 0123456789012345678901234567890123456789 -o crack.exe
```

`crack303.py`将打印必要的日志信息，用以告知运行记录或错误信息

若无报错，生成的`crack.exe`的作者抽水钱包已被替换为`0123456789012345678901234567890123456789`（这里的`0123456789...`只是一个示例钱包地址，实际替换时用个人钱包即可）

使用时，在E池挖矿地址（本例中是 https://ethermine.org/miners/0123456789012345678901234567890123456789/dashboard ）会看到一个名为`devfee303`的矿工，这就是作者抽水，现在都属于你了

## 注意

* 303web版前端会有重复统计矿机名的问题，对真实矿机连接、数目、算力和抽水等无影响。303的性能和稳定性不亚于其它任何中转软件

* 303web版不支持直接在网页上修改抽水比例，若要修改需修改`config.yml`配置文件中的`devfee`字段，并重启软件生效

* 据 @Char1esOrz，303作者抽水为阶梯抽水
  * 0 < 抽水 <= 5，作者抽水 = 0.5
  * 5 < 抽水 <= 10，作者抽水 = 1
  * 10 < 抽水 <= 20，作者抽水 = 2
  * 否则，作者抽水 = 抽水。当抽水50时双方对半

破解后用户拿到所有抽水收益，有效防止 @Char1esOrz 暗抽

## 附录（内容供高级用户参考）

### 1. md5.py

`md5.py`用于打印一个文件的md5（什么是md5自行百度），用以比较一个文件较之前是否有所改动，用法：

```
python md5.py -f FILE
```

`FILE`为要获取md5的文件

@Char1esOrz 303原版的md5如下：（ @Char1esOrz 303原版下载地址：https://github.com/Char1esOrz/minerProxy/releases/tag/v3.0.3 ）

```
linux:

minerProxy/minerProxy_cmd:      600db2c8eb0d89652b1e60fe03e95e83
minerProxy_config:              86147c12411c69c36c258efdc0521a5a
minerProxy_web:                 1418d75af86422677c335f7bab8c7a08

windows:

minerProxy/minerProxy_cmd.exe:  6ef188e71741a3ec9857b65e8f50dd34
minerProxy_config.exe:          7a33191c41dd09846791819af00ee920
minerProxy_web.exe:             eda11b2b35c653fd36dbf3363c6c52d5
```

### 2. plot.py

`plot.py`用于显示303作者阶梯抽水示意图，效果见[plot.png](https://github.com/minerproxycracked/minerProxyCrack/blob/main/plot.png)或下图，用法（需安装所需依赖，自行百度）：

```
python plot.py
```

![avatar](https://i.postimg.cc/HWBkLKNG/plot.png)

## 备份

| | 原地址 | 备份地址 |
| :-----:| :----: | :----: |
| 某盗版303 | https://github.com/minerproxyeth/minerproxy | https://github.com/minerproxycracked/minerproxyeth-minerproxy |
| @Char1esOrz 仓库地址 | https://github.com/Char1esOrz/minerProxy | https://github.com/minerproxycracked/Char1esOrz-minerProxy |
| @Char1esOrz 各版本下载地址 | https://github.com/Char1esOrz/minerProxy/tags | https://github.com/minerproxycracked/Char1esOrz-minerProxy/tags |
| @Char1esOrz 303原版下载地址 | https://github.com/Char1esOrz/minerProxy/releases/tag/v3.0.3 | https://github.com/minerproxycracked/Char1esOrz-minerProxy/releases/tag/v3.0.3 |

请注意 @Char1esOrz 随时可能增加暗抽比例

## 其它

觉得好用可以点个star或fork

捐赠：0x39B849857425643B0036fd932D705cA61BDCF4e9
