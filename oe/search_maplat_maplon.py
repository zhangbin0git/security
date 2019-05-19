#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019-5-19 16:52 
# @Author : Mark 
# @Site :  
# @File : search_maplat_maplon.py 
# @Software: PyCharm Community Edition

import mechanicalsoup

def wigle_print (username, password, netid):
    #  登录wigle根据mac查询经纬度
    # 打开的网址
    URL = 'https://wigle.net/'
    # 建立实例
    browser = mechanicalsoup.StatefulBrowser(
        session=None,
        soup_config={'features': 'lxml'},
        raise_on_404=True)
    # Uncomment for a more verbose output:
    # browser.set_verbose(2)
    browser.open(URL)
    # 选择form, 根据css定位
    browser.select_form('#loginForm')
    # 打印全部内容
    browser.get_current_form().print_summary()
    print('-----------------------------------')
    browser["credential_0"] = username
    browser["credential_1"] = password
    # launch_browser()将在我们的browser 对象访问的当前页面上启动一个真实的Web浏览器，
    # 包括我们刚刚对表单所做的更改（请注意，它不会打开真实的网页，但会创建一个包含页面内
    # 容的临时文件，并指向您的浏览器这个文件）
    # browser.launch_browser()
    # 显示当前form的内容
    browser.get_current_form().print_summary()
    print('-------------------------------')
    # 提交
    resp = browser.submit_selected()
    # 显示返回值
    print(resp.text)
    # 显示url
    print(browser.get_url())
    # 跳转查询界面
    browser.open('https://wigle.net/search')
    # 打印界面
    # print(browser.get_current_page())
    # 定位查询form
    # browser.select_form('#searchForm')
    browser.select_form('form[action="https://api.wigle.net/api/v2/network/search"]')
    print('------------------11111111111111111111')
    browser.get_current_form().print_summary()
    print('-------------------------------')
    browser["ssidlike"] = netid
    browser.get_current_form().print_summary()
    # 提交
    resp1 = browser.submit_selected()
    print(resp1.text)
    # 显示url
    print(browser.get_url())

    # 例外一种方式
    # browser = mechanicalsoup.Browser(soup_config={'features': 'lxml'})
    # login_page = browser.get(URL)
    # login_page.raise_for_status()
    # login_form = mechanicalsoup.Form(login_page.soup.select_one('#loginForm'))
    # login_form.print_summary()
    # print('-----------------------------------')
    # login_form.input({"credential_0":username, "credential_1":password,
    #                   'noexpire':'on'})
    # login_form.print_summary()
    # repon = browser.submit(login_form, login_page.url)
    # print(repon.text)
    # print(browser.get('https://wigle.net/search').text)

    map_lat = 'N/A'
    map_lon = 'N/A'


if __name__ == '__main__':
    wigle_print('air8sky', 'zlx520..', 'zhangbin')