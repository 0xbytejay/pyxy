import requests
# 我在校园API--START

# 我在校园基本请求
def baseApi(path,method,payload,jwsession,referer):
    url = "https://gw.wozaixiaoyuan.com"+path
    headers = {
        'Host': 'gw.wozaixiaoyuan.com',
        'accept': 'application/json, text/plain, */*',
        'jwsession': jwsession,
        'user-agent': 'Mozilla/5.0 (Linux; Android 7.1.2; P40 Build/NZH54D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3149 MMWEBSDK/20211001 Mobile Safari/537.36 MMWEBID/7352 MicroMessenger/8.0.16.2040(0x28001037) Process/appbrand0 WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 miniProgram/wxce6d08f781975d91',
        'content-type': 'application/json;charset=UTF-8',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': referer,
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8'
    }
    response = requests.request(method, url, headers=headers, data=payload)
    return  response.text

# 密码登录接口
def loginBypassword(username,password):
    res = baseApi("/basicinfo/mobile/login/username?username=%s&password=%s&openId=o0-5d1nopNszHFJ4hBNWwGOXdry4&unionId=oUXUs1QDV5fwIiG1IuDUl25gyHRI&phoneInfo=1____linux%3B+android+7.1.2%3B+p40+build%2Fnzh54d%3B+wv"%(username,password),
                  "GET",
                  {},
                  "",
                  "https://gw.wozaixiaoyuan.com/h5/mobile/basicinfo/index/login/index?jwcode=1002&openId=o0-5d1nopNszHFJ4hBNWwGOXdry4&unionId=oUXUs1QDV5fwIiG1IuDUl25gyHRI")
    return res

# 使用旧密码重置密码
def resetPasswordByOldpassword(password,vercode,jwsession):
    return baseApi("/basicinfo/mobile/my/changePassword?newPassword=%s&oldPassword=%s&code=%s"%(password,password,vercode),
                   "GET",
                   {},
                   "https://gw.wozaixiaoyuan.com/h5/mobile/basicinfo/index/my/changePassword")

# 使用验证码重置密码
def resetPasswordByVercode(phone,vercode,password):
    res=baseApi("/basicinfo/mobile/login/changePassword?phone=%s&code=%s&password=%s"%(phone,vercode,password),
                "GET",
                {},
                "",
                "https://gw.wozaixiaoyuan.com/h5/mobile/basicinfo/index/login/changePassword")
    return res

# 获取用户信息，可用于判断token是否失效，以及用户身份是否正确
def getUserInfo(jwsession):
    res=baseApi("/basicinfo/mobile/home/index?miniAppId=&env=0",
                "POST",
                {},
                jwsession,
                "https://gw.wozaixiaoyuan.com/h5/mobile/basicinfo/index")
    return res

# 上传打卡信息
def postHealthStatus(jwsession,payload):
    # payload参考
    '''
    {
    answers:["0","1","36.0","无"], //此项需要根据学校动态改变
    latitude=维度（3-53）,
    longitude=经度（135-73）,
    country=中国,
    province=xx省,
    city=xx市,
    district=xx区,
    township=xx街道,
    street=xx路,
    areacode=当地身份证前六位,
    }
    '''
    res=baseApi(path="/health/save.json",
                method="POST",
                payload=payload,
                jwsession=jwsession,
                referer="https://servicewechat.com/wxce6d08f781975d91/181/page-frame.html")
    return res

#


# 我在校园API--END