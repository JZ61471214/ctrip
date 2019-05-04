from appium import webdriver


def initDriver():
    desired_caps = dict()
    desired_caps["platformName"] = "android"
    desired_caps["platformVersion"] = "5.1.1"
    desired_caps["deviceName"] = "*****"
    # desired_caps["appPackage"] = "com.android.settings"
    # desired_caps["appActivity"] = ".Settings"
    desired_caps["appPackage"] = "ctrip.android.view"
    desired_caps["appActivity"] = "ctrip.business.splash.CtripSplashActivity"
    desired_caps["resetKeyboard"] = True
    desired_caps["unicodeKeyboard"] = True
    desired_caps["noReset"] = True
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    return driver

