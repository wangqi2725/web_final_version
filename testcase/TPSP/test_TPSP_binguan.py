# coding:utf-8

from selenium import webdriver
import unittest
import time,os
from public.common import mytest
from public.pages import login_page
from public.common import datainfo
from public.common.publicfunction import get_img
from faker import Factory



class Test_basic(mytest.MyTest):
    '''
    用例编号：
    模块：
    功能点：
    测试点描述：
    测试步骤：

    预期结果：

    '''

    def test_basic_test(self):
        """演示脚本"""
        #************************** login ************************
        page = login_page.IndexPage(self.dr)
        page.into_page('http://192.168.0.65:8010/')
        page.input_username_key('admin')
        page.input_password_key('123456')
        page.click_button()
        time.sleep(7)

        #************************** porject ***********************
        self.dr.click('id->systemName')
        time.sleep(1)

        self.dr.click('xpath->/html/body/div[1]/ul/li[2]/ul/li[5]')
        time.sleep(3)

        self.dr.click('id->551')#基础数据配置
        time.sleep(2)

        self.dr.click('id->642')#宾馆酒店
        time.sleep(3)

        #************************ 切换frame **********************
        self.dr.switch_to_frame('id->indIframe')
        time.sleep(3)

        #************************* before check ********************
        text_before = self.dr.get_text('xpath->/html/body/div[2]/div/div[2]/div[2]/div/span')#当前*页，共*页，合计*条

        #************************** actions ************************
        self.dr.click('id->listAddButton')#添加
        time.sleep(3)
        self.dr.type('name->name','中国')#名称

        self.dr.click('xpath->//*[@id="regionSelector"]/div[3]')
        time.sleep(2)
        self.dr.click('xpath->//*[@id="regionSelector"]/div[3]/ul/li[2]')#所属地区

        self.dr.type('name->shortname','BG')#缩略名称

        self.dr.click('id->mbBox9')
        time.sleep(3)
        self.dr.click('xpath->//*[@id="messMap"]/div[1]/div[1]')
        time.sleep(3)
        self.dr.click('xpath->/html/body/div[4]/div[2]/div[1]/div/a')#经纬度
        time.sleep(3)

        self.dr.click('id->logoUploadBox_1_1')
        time.sleep(2)
        os.system('D:\WinClick.exe')#形象标识1:1
        time.sleep(2)

        self.dr.click('xpath->//*[@id="dataForm"]/div[2]/div/button')#确认提交

        #************************ check after ************************
        #check 1:数量变化
        text_fater = self.dr.get_text('xpath->/html/body/div[2]/div/div[2]/div[2]/div/span')
        # text_before equal text_fater
        if text_before == text_fater:
            pass
        else:
            raise SystemError

