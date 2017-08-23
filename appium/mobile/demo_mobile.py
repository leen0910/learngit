# coding:utf-8
import os,time, unittest
import datetime
import HTMLTestRunner
from appium import webdriver
import traceback
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
import sys



PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))


class QXmobile(unittest.TestCase):
    # 全局启动app
    @classmethod
    def setUpClass(cls):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'  # 版本号　
        desired_caps['deviceName'] = 'ZTEBA510' # 设备名称
        # desired_caps['app']= PATH(r"D:\gitblit\mobile.qixing-group.com\platforms\android\build\outputs\apk\android-x86-debug.apk")　
        desired_caps['appPackage'] = 'robot.qixing.mobile'
        desired_caps['appActivity'] = 'robot.qixing.mobile.MainActivity'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True#屏蔽软键盘

        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 启动app

        print("start app")
    # 启动app强制等待时间
    def test_sleep(self):
        time.sleep(20)
        print("sleep passed")

    # 全局退出
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("tearDown")

    def login(self):
        time.sleep(10)
        self.driver.find_element_by_xpath("//android.widget.EditText[contains(@text,'ln')]").clear()
        time.sleep(2)
        self.driver.find_element_by_xpath("//android.widget.EditText[contains(@text,'用户名')]").send_keys("ln")
        time.sleep(2)
        self.driver.find_element_by_xpath("//android.widget.EditText[contains(@text,'••••••')]").clear()
        time.sleep(2)
        self.driver.find_element_by_xpath("//android.widget.EditText[contains(@text,'密码')]").send_keys("ln")
        time.sleep(2)
        self.driver.find_element_by_xpath("//android.widget.Button[contains(@content-desc,'登 录 ')]").click()
        time.sleep(2)
        try:
            # self.driver.find_element_by_class_name("android.app.Dialog").is_displayed()
            self.driver.find_element_by_xpath("//android.widget.Button[contains(@content-desc,'确定')]").is_displayed()
            print("用户登录失败")
            self.driver.get_screenshot_as_file("./image/"+'用户登录失败'+'.jpg')
            time.sleep(2)
            self.clickScreen()
            time.sleep(2)
        except:
            pass
            self.driver.get_screenshot_as_file("./image/"+'success_login'+'.jpg')
            print("用户：ln/ln 登录成功")
        time.sleep(10)

    def login_quit(self):
        time.sleep(10)
        self.driver.find_element_by_xpath("//android.widget.EditText[contains(@text,'用户名')]").send_keys("ln")
        time.sleep(3)
        self.driver.find_element_by_xpath("//android.widget.EditText[contains(@text,'密码')]").send_keys("ln")
        time.sleep(2)
        self.driver.find_element_by_xpath("//android.widget.Button[contains(@content-desc,'登 录 ')]").click()
        time.sleep(2)
        try:
            # self.driver.find_element_by_class_name("android.app.Dialog").is_displayed()
            self.driver.find_element_by_xpath("//android.widget.Button[contains(@content-desc,'确定')]").is_displayed()
            print("用户登录失败")
            self.driver.get_screenshot_as_file("./image/"+'用户登录失败'+'.jpg')
            time.sleep(2)
            self.clickScreen()
            time.sleep(2)
        except:
            pass
            self.driver.get_screenshot_as_file("./image/"+'success_login'+'.jpg')
            print("用户：ln/ln登录成功")
        time.sleep(10)

    # 偿试元素定位，主界面tab切换。不同设备主键值会有变化，目前调试pad
    def switch_tab(self):
        time.sleep(10)
        # el1=self.driver.find_element_by_xpath("//android.view.View[contains(@resource_id,'tab-t0-0')]")
        # el2=self.driver.find_element_by_xpath("//android.view.View[contains(@resource_id,'tab-t0-1')]")
        # el3=self.driver.find_element_by_xpath("//android.view.View[contains(@resource_id,'tab-t0-2')]")
        # el=self.driver.find_elements_by_class_name("android.view.View")
        el1=self.driver.find_element_by_name("home1 程序 ")
        el2=self.driver.find_element_by_name("patameter 参数 ")
        el3=self.driver.find_element_by_name("equipment 设备 ")
        el1.click()
        time.sleep(5)
        count=2
        print("压力测试次数:%s" % (count*3))
        while count>0:
            el3.click()
            el2.click()
            el1.click()
            count=count-1
            self.driver.get_screenshot_as_file("./image/"+'switch_tab_%s'% count+'.jpg')
        print("TAB页的切换的压力测试通过")

    # 方法得到屏幕尺寸
    def getSize(self):
        x=self.driver.get_window_size()['width']
        y=self.driver.get_window_size()['height']
        return(x,y)
        print("得到屏幕尺寸:%s，%s" % (x,y))

    # 方法下拉刷新屏幕
    def refreshScreen(self,t):
        l=self.getSize()
        x1=int(l[0]*0.5)
        y1=int(l[1]*0.25)
        y2=int(l[1]*0.85)
        self.driver.swipe(x1,y1,x1,y2,t)
        try:
            # self.driver.find_element_by_xpath("//android.widget.Button[contains(@content-desc,'确定')]").is_displayed()
            self.driver.find_element_by_class_name("android.app.Dialog").is_displayed()
            print("刷新列表出错")
            self.driver.get_screenshot_as_file("./image/"+'刷新文件列出错'+'.jpg')
            self.clickScreen()
        except:
            print("刷新列表成功")

    # 方法点击屏幕
    def clickScreen(self):
        l=self.getSize()
        x=int(l[0]*0.5)
        y=int(l[1]*0.8)
        self.driver.tap([(x,y)],2)
        time.sleep(4)

    # 方法控件左滑
    def swipeLeft(self,pel):
        start=pel.location
        print("控件起始位置：%s" % start)
        self.driver.swipe(start['x']+100,start['y'],start['x']-100,start['y'],2000)

    # 方法控件右滑
    def swipeRight(self,pel):
        start=pel.location
        print("控件起始位置：%s" % start)
        self.driver.swipe(start['x'],start['y'],start['x']+200,start['y'],2000)

    # 设备页面下拉刷新
    def refresh_device(self):
        time.sleep(10)
        # self.driver.find_element_by_xpath("//android.view.View[contains(@resource_id,'tab-t0-2')]").click()
        self.driver.find_element_by_name("equipment 设备 ").click()
        l=self.getSize()
        x1=int(l[0]*0.5)
        y1=int(l[1]*0.25)
        y2=int(l[1]*0.75)
        print("选择下拉屏幕的坐标:%s,%s" % (x1,y1))
        count=3
        print("下拉刷新次数：%s" % count)
        while count>0:
            self.driver.swipe(x1,y1,x1,y2,700)
            # self.driver.swipe(403,545,407,1000,600)
            time.sleep(3)
            # self.driver.get_screenshot_as_file("./image/"+time.strftime('%Y%m%d%H%M%S')+'.jpg')
            self.driver.get_screenshot_as_file("./image/"+'refresh_device_%s次'% count+'.jpg')
            print("刷新设备列%s次成功" % count)
            count=count-1
        print("刷新设备列表压力测试通过")

    # 选择任一个可控设备
    def Select_device(self):
        time.sleep(3)
        self.driver.find_element_by_name("equipment 设备 ").click()
        time.sleep(2)
        self.refreshScreen(700)
        time.sleep(5)
        try:
            self.driver.find_element_by_xpath("//android.view.View[contains(@content-desc,'控制中')]").is_displayed()
            print("正在控制设备")
        except:
            try:
                self.driver.find_element_by_xpath("//android.view.View[contains(@content-desc,'可控')]").is_displayed()
                print("有可控设备")
                try:
                    time.sleep(2)
                    self.driver.find_element_by_xpath("//android.view.View[contains(@content-desc,'可控')]").click()
                    print("成功控制设备")
                    time.sleep(2)
                    self.driver.get_screenshot_as_file("./image/"+'control_device'+'.jpg')
                    time.sleep(4)
                except Exception as e:
                    print(Exception,e)
            except:
                print("没有可控设备")
                self.driver.get_screenshot_as_file("./image/"+'invalid_device'+'.jpg')

    # 释放控制的设备
    def Release_device(self):
        time.sleep(1)
        self.driver.find_element_by_name("equipment 设备 ").click()
        time.sleep(2)
        self.refreshScreen(700)
        time.sleep(5)
        try:
            self.driver.find_element_by_xpath("//android.view.View[contains(@content-desc,'控制中')]").is_displayed()
            print('设备控制中')
            self.driver.find_element_by_xpath("//android.view.View[contains(@content-desc,'控制中')]").click()
            print('成功释放设备')
            time.sleep(3)
        except:
            print("无控制中的设备")

    # 用户中心drawer
    def user_center(self):
        time.sleep(1)
        l1=self.getSize()
        x1=int(l1[0]*0.75)
        y1=int(l1[1]*0.5)
        x2=int(l1[0]*0.25)
        count=2
        print("多次开启关闭用户中心的压力测试： %s" % count)
        while count>0:
            self.driver.find_element_by_class_name("android.widget.Button").click()
            time.sleep(1)
            self.driver.swipe(x1,y1,x2,y1,300)
            count=count-1
        print("用户中心控件压力测试通过")

    # 程序列表操作
    def program_files(self):
        self.driver.find_element_by_name("home1 程序 ").click()
        time.sleep(1)
        self.refreshScreen(700)
        time.sleep(2)
        try:
            pel=self.driver.find_element_by_xpath("//android.view.View[contains(@resource-id,'lbl')]")
            print("找到程序文件")
            self.swipeLeft(pel)
            # start=pel.location
            # print(start)
            # self.driver.swipe(start['x']+200,start['y'],start['x']-100,start['y'],2000)
            # self.driver.get_screenshot_as_file("./image/"+"左滑程序文件"+'.jpg')
            print("程序文件列向左滑动")
            self.driver.get_screenshot_as_file("./image/"+"swipe_program_left"+'.jpg')
            time.sleep(3)
            try:
                self.driver.find_element_by_xpath("//android.widget.Button[contains(@content-desc,'上传')]").click()
                time.sleep(3)
                try:
                    # self.driver.find_element_by_xpath("//android.widget.Button[contains(@content-desc,'确定')]").is_displayed()
                    self.driver.find_element_by_class_name("android.app.Dialog").is_displayed()
                    print("上传程序错误")
                    self.driver.get_screenshot_as_file("./image/"+'上传文件失败'+'.jpg')
                    self.clickScreen()
                except:
                    print("上传程序文件到云端成功")
            except Exception as e:
                print(Exception,e)
                self.driver.get_screenshot_as_file("./image/"+'upload_program_erro'+'.jpg')
            time.sleep(3)
            self.swipeRight(pel)
            self.driver.get_screenshot_as_file("./image/"+'program_restore_button'+'.jpg')
            time.sleep(2)
            try:
                self.driver.find_element_by_xpath("//android.widget.Button[contains(@content-desc,'恢复')]").click()
                time.sleep(2)
                try:
                    self.driver.find_element_by_xpath("//android.widget.Button[contains(@content-desc,'确定')]").is_displayed()
                    # self.driver.find_element_by_class_name("android.app.Dialog").is_displayed()
                    print("从云端恢复文件错误")
                    self.driver.get_screenshot_as_file("./image/"+'云端恢复文件失败'+'.jpg')
                    self.clickScreen()
                except:
                    print("云端恢复程序文件成功")
            except Exception as e:
                print(Exception,e)
                self.driver.get_screenshot_as_file("./image/"+'云端恢复程序错误'+'.jpg')
        except:
            pass
            print("无程序文件列表 ")
            self.driver.get_screenshot_as_file("./image/"+'无程序文件'+'.jpg')
        time.sleep(3)

    # 参数文件列表：上传删除恢复
    def settings_files(self):
        self.driver.find_element_by_name("patameter 参数 ").click()
        time.sleep(1)
        self.refreshScreen(700)
        time.sleep(2)
        try:
            pel=self.driver.find_element_by_xpath("//android.view.View[contains(@resource-id,'lbl')]")
            print("找到参数文件")
            self.swipeLeft(pel)
            print("参数文件列向左滑动")
            self.driver.get_screenshot_as_file("./image/"+"swipe_settings_left"+'.jpg')
            time.sleep(2)
            try:
                self.driver.find_element_by_xpath("//android.widget.Button[contains(@content-desc,'上传')]").click()
                time.sleep(3)
                try:
                    # self.driver.find_element_by_xpath("//android.widget.Button[contains(@content-desc,'确定')]").is_displayed()
                    self.driver.find_element_by_class_name("android.app.Dialog").is_displayed()
                    print("上传参数错误")
                    self.driver.get_screenshot_as_file("./image/"+'上传参数失败'+'.jpg')
                    self.clickScreen()
                except:
                    print("上传参数文件到云端成功")
            except Exception as e:
                print(Exception,e)
                self.driver.get_screenshot_as_file("./image/"+'upload_settings file_erro'+'.jpg')
            time.sleep(3)
            self.swipeRight(pel)
            self.driver.get_screenshot_as_file("./image/"+'settings_restore'+'.jpg')
            time.sleep(3)
            try:
                self.driver.find_element_by_xpath("//android.widget.Button[contains(@content-desc,'云端')]").click()
                time.sleep(3)
                try:
                    # self.driver.find_element_by_xpath("//android.widget.Button[contains(@content-desc,'确定')]").is_displayed()
                    self.driver.find_element_by_class_name("android.app.Dialog").is_displayed()
                    print("从云端恢复参数错误")
                    self.driver.get_screenshot_as_file("./image/"+'云端恢复参数失败'+'.jpg')
                    self.clickScreen()
                except:
                    print("云端参数恢复文件成功")
            except Exception as e:
                print(Exception,e)
                self.driver.get_screenshot_as_file("./image/"+'云端恢复参数_erro'+'.jpg')
        except:
            pass
            print("不存在参数文件列表")
            self.driver.get_screenshot_as_file("./image/"+'不存在参数列表'+'.jpg')
        time.sleep(5)

    # 搜索功能
    def search(self,cha):
        self.driver.find_element_by_class_name("android.widget.EditText").click()
        self.driver.find_element_by_class_name("android.widget.EditText").send_keys(cha)
        time.sleep(5)

    # 打开路点示教页，前提要先device_select
    def point_teach(self):
        self.driver.find_element_by_name("home1 程序 ").click()
        # self.refreshScreen(700)
        time.sleep(5)
        try:
            self.driver.find_element_by_xpath("//android.view.View[contains(@resource-id,'lbl')]").is_displayed()
            print('找到程序文件')
            time.sleep(3)
            self.driver.find_element_by_xpath("//android.view.View[contains(@resource-id,'lbl')]").click()
            time.sleep(3)
            try:
                # self.driver.find_element_by_xpath("//android.widget.Button[contains(@content-desc,'确定')]").is_displayed()
                self.driver.find_element_by_class_name("android.app.Dialog").is_displayed()
                print("打开程序树失败")
                self.driver.get_screenshot_as_file("./image/"+'程序树打开失败'+'.jpg')
                self.clickScreen()
                time.sleep(1)
            except:
                try:
                    self.search(u"路")
                    time.sleep(4)
                    self.driver.find_element_by_xpath("//android.view.View[contains(@content-desc,'路点')]").is_displayed()
                    time.sleep(1)
                    self.driver.find_element_by_xpath("//android.view.View[contains(@content-desc,'路点')]").click()
                    time.sleep(3)
                    print('打开路点示教页')
                    self.driver.keyevent(4)
                    print("返回程序树页面")
                    self.driver.get_screenshot_as_file("./image/"+'point_teach'+'.jpg')
                except:
                    print("无路点节点，无法进入示教")
                    time.sleep(2)
                self.driver.keyevent(4)
                print("返回程序列表页")
                time.sleep(2)
        except Exception as e:
            print(Exception,e)



    # 删除一个程序文件
    def delete_program(self):
        self.driver.find_element_by_name("home1 程序 ").click()
        time.sleep(2)
        self.refreshScreen(700)
        time.sleep(3)
        pel=self.driver.find_element_by_xpath("//android.view.View[contains(@resource-id,'lbl')]")
        print("找到程序文件")
        self.swipeLeft(pel)
        time.sleep(1)
        self.driver.find_element_by_xpath("//android.widget.Button[contains(@content-desc,'删除')]").click()
        time.sleep(3)
        try:
            self.driver.find_element_by_class_name("android.app.Dialog").is_displayed()
            # self.driver.find_element_by_xpath("//android.widget.Button[contains(@content-desc,'确认')]").is_displayed()
            self.driver.find_element_by_xpath("//android.widget.Button[contains(@content-desc,'确认')]").click() #"确认"为删除
            print("确认删除")
            time.sleep(3)
            try:
                self.driver.find_element_by_class_name("android.app.Dialog").is_displayed()
                # self.driver.find_element_by_xpath("//android.widget.Button[contains(@content-desc,'确定')]").is_displayed()
                print("删除程序失败")
                self.driver.get_screenshot_as_file("./image/"+'删除程序文件失败'+'.jpg')
                time.sleep(2)
                self.clickScreen()
                time.sleep(2)
            except:
                pass
        except Exception as e:
            print(Exception,e)
            self.driver.get_screenshot_as_file("./image/"+'删除程序_error1'+'.jpg')

     # 删除一个参数文件
    def delete_settings(self):
        self.driver.find_element_by_name("patameter 参数 ").click()
        time.sleep(2)
        self.refreshScreen(700)
        time.sleep(3)
        pel=self.driver.find_element_by_xpath("//android.view.View[contains(@resource-id,'lbl')]")
        print("找到参数文件")
        self.swipeLeft(pel)
        time.sleep(1)
        self.driver.find_element_by_xpath("//android.widget.Button[contains(@content-desc,'删除')]").click()
        time.sleep(3)
        try:
            self.driver.find_element_by_class_name("android.app.Dialog").is_displayed()
            # self.driver.find_element_by_xpath("//android.widget.Button[contains(@content-desc,'确认')]").is_displayed()
            self.driver.find_element_by_xpath("//android.widget.Button[contains(@content-desc,'确认')]").click() #"确认"为删除
            print("确认删除")
            time.sleep(4)
            try:
                self.driver.find_element_by_class_name("android.app.Dialog").is_displayed()
                # self.driver.find_element_by_xpath("//android.widget.Button[contains(@content-desc,'确定')]").is_displayed()
                print("删除参数失败")
                self.driver.get_screenshot_as_file("./image/"+'删除参数文件失败'+'.jpg')
                time.sleep(2)
                self.clickScreen()
                time.sleep(2)
            except:
                pass
        except Exception as e:
            print(Exception,e)
            self.driver.get_screenshot_as_file("./image/"+'删除参数_error1'+'.jpg')

    # 用户中心菜单
    def drawer_menu(self):
        l1=self.getSize()
        x1=int(l1[0]*0.75)
        y1=int(l1[1]*0.5)
        x2=int(l1[0]*0.25)
        time.sleep(5)
        self.driver.find_element_by_class_name("android.widget.Button").click()
        time.sleep(2)
        try:
            # self.driver.find_element_by_name('用户信息').click()
            # self.driver.find_element_by_xpath("//android.view.View[contains(@content-desc,'用户信息')]").click()
            self.driver.tap([(252,525)],1)  #此菜单元素定位一直没响应，改为坐标值定位
            time.sleep(1)
            try:
                self.driver.find_element_by_xpath("//android.webkit.WebView[contains(@content-desc,'用户信息')]").is_displayed()
                self.driver.get_screenshot_as_file("./image/"+'open_user_info'+'.jpg')
                print("查看用户信息")
                self.driver.keyevent(4)
                time.sleep(3)
            except:
                print("无法打开用户信息")
        except:
            print("打开用户信息错误")
            self.driver.get_screenshot_as_file("./image/"+'打开用户信息错误'+'.jpg')
        try:
            self.driver.find_element_by_name('关于我们').click()
            # self.driver.find_element_by_xpath("//android.view.View[contains(@content-desc,'关于我们')]").click()
            time.sleep(1)
            try:
                self.driver.find_element_by_xpath("//android.webkit.WebView[contains(@content-desc,'关于我们')]").is_displayed()
                self.driver.get_screenshot_as_file("./image/"+'open_about_us'+'.jpg')
                print("打开关于我们")
                self.driver.keyevent(4)
                time.sleep(3)
            except:
                print("无法打开关于我们")
        except:
            print("打开用户信息错误")
            self.driver.get_screenshot_as_file("./image/"+'打开关于我们错误'+'.jpg')
        # try:
        #     self.driver.find_element_by_name('版本信息').click()
        #     # self.driver.find_element_by_xpath("//android.view.View[contains(@content-desc,'版本信息')]").click()
        #     time.sleep(1)
        #     try:
        #         self.driver.find_element_by_xpath("//android.webkit.WebView[contains(@content-desc,'版本更新')]").is_displayed()
        #         self.driver.get_screenshot_as_file("./image/"+'open_version'+'.jpg')
        #         print("查看版本信息")
        #         self.driver.keyevent(4)
        #         time.sleep(3)
        #     except:
        #         print("无法打开版本信息")
        # except:
        #     print("打开版本信息错误")
        #     self.driver.get_screenshot_as_file("./image/"+'打开版本信息错误'+'.jpg')

        try:
            time.sleep(1)
            self.driver.find_element_by_name('意见反馈').click()
            # self.driver.find_element_by_xpath("//android.view.View[contains(@content-desc,'意见反馈')]").click()
            time.sleep(1)
            try:
                self.driver.find_element_by_xpath("//android.webkit.WebView[contains(@content-desc,'意见反馈')]").is_displayed()
                self.driver.get_screenshot_as_file("./image/"+'open_feedback'+'.jpg')
                print("打开意见反馈")
                time.sleep(2)
                # self.driver.find_element_by_xpath("//android.widget.RadioButton[contains(@content-desc,'建议')]").click()
                self.driver.find_element_by_xpath("//android.widget.EditText[contains(@resource-id,'suggestReport')]").send_keys("feedbacktest")
                time.sleep(2)
                self.driver.find_element_by_xpath("//android.widget.Button[contains(@content-desc,'提交')]").click()
                # self.driver.tap([(330,1075)],1)  #此菜单元素定位位置有偏移，无效点击，改为坐标值定位
                time.sleep(2)
                self.driver.get_screenshot_as_file("./image/"+'submit_feedback'+'.jpg')
                try:
                    self.driver.find_element_by_xpath("//android.view.View[contains(@content-desc,'提交成功')]").is_displayed()
                    self.driver.find_element_by_xpath("//android.widget.Button[contains(@content-desc,'确定 ')]").click()
                    print("成功提交反馈")
                    time.sleep(3)
                except:
                    print("提交反馈失败")
                    self.driver.get_screenshot_as_file("./image/"+'提交反馈失败_'+'.jpg')
                    self.clickScreen()
                    time.sleep(1)
                    self.driver.keyevent(4)
                    time.sleep(2)
            except:
                print("无法打开意见反馈")

        except:
            print("打开意见反馈错误")
            self.driver.get_screenshot_as_file("./image/"+'打开意见反馈错误'+'.jpg')

        self.driver.swipe(x1,y1,x2,y1,300)
        time.sleep(4)

    # 用户中心菜单--退出
    def drawer_menu_quit(self):
        l1=self.getSize()
        x1=int(l1[0]*0.75)
        y1=int(l1[1]*0.5)
        x2=int(l1[0]*0.25)
        time.sleep(5)
        self.driver.find_element_by_class_name("android.widget.Button").click()
        time.sleep(2)
        try:
            # self.driver.find_element_by_name('用户信息').click()
            self.driver.find_element_by_xpath("//android.view.View[contains(@content-desc,'用户信息')]").click()
            # self.driver.tap([(252,525)],1)  #此菜单元素定位一直没响应，改为坐标值定位
            time.sleep(1)
            try:
                self.driver.find_element_by_xpath("//android.webkit.WebView[contains(@content-desc,'用户信息')]").is_displayed()
                self.driver.get_screenshot_as_file("./image/"+'open_user_info'+'.jpg')
                print("查看用户信息")
                self.driver.keyevent(4)
                time.sleep(3)
            except:
                print("无法打开用户信息")
        except:
            print("没有找到用户信息")
            self.driver.get_screenshot_as_file("./image/"+'没有找到用户信息'+'.jpg')
        try:
            self.driver.find_element_by_name('关于我们').click()
            # self.driver.find_element_by_xpath("//android.view.View[contains(@content-desc,'关于我们')]").click()
            time.sleep(1)
            try:
                self.driver.find_element_by_xpath("//android.webkit.WebView[contains(@content-desc,'关于我们')]").is_displayed()
                self.driver.get_screenshot_as_file("./image/"+'open_about_us'+'.jpg')
                print("打开关于我们")
                self.driver.keyevent(4)
                time.sleep(3)
            except:
                print("无法打开关于我们")
        except:
            print("没有找到关于我们")
            self.driver.get_screenshot_as_file("./image/"+'没有找到关于我们'+'.jpg')
        try:
            self.driver.find_element_by_name('版本信息').click()
            # self.driver.find_element_by_xpath("//android.view.View[contains(@content-desc,'版本信息')]").click()
            time.sleep(1)
            try:
                self.driver.find_element_by_xpath("//android.webkit.WebView[contains(@content-desc,'版本更新')]").is_displayed()
                self.driver.get_screenshot_as_file("./image/"+'open_version'+'.jpg')
                print("查看版本信息")
                self.driver.keyevent(4)
                time.sleep(3)
            except:
                print("无法打开版本信息")
        except:
            print("没有找到版本信息")
            self.driver.get_screenshot_as_file("./image/"+'没有找到版本信息'+'.jpg')

        try:
            time.sleep(1)
            self.driver.find_element_by_name('意见反馈').click()
            # self.driver.find_element_by_xpath("//android.view.View[contains(@content-desc,'意见反馈')]").click()
            time.sleep(1)
            try:
                self.driver.find_element_by_xpath("//android.webkit.WebView[contains(@content-desc,'意见反馈')]").is_displayed()
                self.driver.get_screenshot_as_file("./image/"+'open_feedback'+'.jpg')
                print("打开意见反馈")
                time.sleep(2)
                # self.driver.find_element_by_xpath("//android.widget.RadioButton[contains(@content-desc,'建议')]").click()
                self.driver.find_element_by_xpath("//android.widget.EditText[contains(@resource-id,'suggestReport')]").send_keys("feedbacktest")
                time.sleep(2)
                self.driver.find_element_by_xpath("//android.widget.Button[contains(@content-desc,'提交')]").click()
                # self.driver.tap([(330,1075)],1)  #此菜单元素定位位置有偏移，无效点击，改为坐标值定位
                time.sleep(2)
                self.driver.get_screenshot_as_file("./image/"+'submit_feedback'+'.jpg')
                try:
                    self.driver.find_element_by_xpath("//android.view.View[contains(@content-desc,'提交成功')]").is_displayed()
                    self.driver.find_element_by_xpath("//android.widget.Button[contains(@content-desc,'确定 ')]").click()
                    print("成功提交反馈")
                    time.sleep(3)
                except:
                    print("提交反馈失败")
                    self.driver.get_screenshot_as_file("./image/"+'提交反馈失败_'+'.jpg')
                    self.clickScreen()
                    time.sleep(1)
                    self.driver.keyevent(4)
                    time.sleep(2)
            except:
                print("无法打开意见反馈")

        except:
            print("没有找到意见反馈")
            self.driver.get_screenshot_as_file("./image/"+'没有找到意见反馈'+'.jpg')

        self.driver.find_element_by_name('退出登录').click()
        print("退出登录")
        time.sleep(4)



if __name__ == '__main__':
    testunit = unittest.TestSuite()  # 定义一个单元测试容器
    testunit.addTest(QXmobile("test_sleep"))
    # testunit.addTest(QXmobile("login"))
    testunit.addTest(QXmobile("login_quit"))
    testunit.addTest(QXmobile("switch_tab"))  # 将测试用例加入到测试容器中
    testunit.addTest(QXmobile("refresh_device"))
    testunit.addTest(QXmobile("user_center"))
    testunit.addTest(QXmobile("Select_device"))
    testunit.addTest(QXmobile("program_files"))
    testunit.addTest(QXmobile("settings_files"))
    testunit.addTest(QXmobile("point_teach"))
    testunit.addTest(QXmobile("delete_program"))
    testunit.addTest(QXmobile("delete_settings"))
    testunit.addTest(QXmobile("Release_device"))
    # testunit.addTest(QXmobile("drawer_menu"))
    testunit.addTest(QXmobile("drawer_menu_quit"))
    timestr = time.strftime("%Y-%m-%d_%H%M%S") #本地日期作为测试报告的名字
    filename = "./"+timestr+".html"
    # filename = "./myAppiumLog.html"
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='QX示教器测试报告',
     description='用例测试情况')  # 使用HTMLTestRunner配置参数，输出报告路径、报告标题、描述
    runner.run(testunit)  # 自动进行测试
    fp.close()
