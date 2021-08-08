'''
<システム名>
ポータルサイトクローリングプログラム「MUSUCA」

<更新履歴>
2019/11/02  Ver.1.20リリース。不動産投資連合体のクローリング。
2019/11/02  Ver.1.00リリース。健美家のクローリング。

<注意事項>
夜間のクローリングを推奨。

<免責>


'''
# --- 使用するモジュールのインポート ----------------------------------------------- #

from urllib.request import urlopen
from bs4 import BeautifulSoup
from getpass import getpass

import urllib.request, urllib.error     # csv作成のため
import requests
import random
import time
import csv
import re
# import os

# --- コンソール画面のクリア ------------------------------------------------------- #

# os.Program('cls')

# --- ディスプレイ ----------------------------------------------------------------- #

print('\n')
print('   +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+')
print('   |                                                                       |')
print('   |                                                                       |')
print('   |                                                                       |')
print('   +                     Portal Site Crawling Program                      +')
print('   |                                                                       |')
print('   |                        M U S U C A Ver.1.20                           |')
print('   |                                                                       |')
print('   +                            for windows                                +')
print('   |                                                                       |')
print('   |                        Last update: 2019.11.5                         |')
print('   |                                                                       |')
# time.sleep(0.05)
print('   +                      Made by Tatsuhide HIRAKAWA                       +')
print('   |                    tatsuhide.hirakawa@hirasyo.com                     |')
print('   |                                                                       |')
print('   +                                                                       +')
print('   |                                                                       |')
print('   |                                                                       |')
print('   +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+\n')

print('   +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+')
print('   |                                                                       |')
print('   |                                                                       |')
print('   |   Exemption                                                           |')
print('   |   * We are not responsible for any damage caused by this program.     |')
print('   |     Use at your own risk.                                             |')
print('   |                                                                       |')
print('   |   Warning                                                             |')
# time.sleep(0.05)
print('   |   * When crawling in large quantities, do it at night.                |')
print('   |   * Make sure to enter alphanumeric characters.                       |')
print('   |                                                                       |')
print('   |                                                                       |')
print('   +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+\n')

print('Initializing MUSUCA Ver.1.20 Program...')
# time.sleep(0.9)
print('Please Wait...')
time.sleep(1.1)

'''
# --- 起動パスワードの入力 --------------------------------------------------------- #

user_db = (
    ('admin@hirasyo.com', 'administrator'),
    ('tatsuhide.hirakawa@hirasyo.com', 'P@aaw0rd'),
    ('guest', 'guest'),
    ('a', 'a'),
    )

user = input('Enter login ID -> ')
pw = getpass('Enter login PW -> ')

if (user, pw) in user_db:
    print("Authentication Successed. Please wait...\n")
else:
    print("Authentication Prosess was Failure...")

'''

# --- クローリング対象サイトの選択 ------------------------------------------------- #

time.sleep(1.3)
print('\n   +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+')
print('   |                                                                       |')
print('   |   Target Site Menu <Fig_1>:                                           |')
print('   |                                                                       |')
print('   +   1 :E-FUDOSAN (http://www.e-fudousanhanbai.com/)                     +')
print('   |   2 :KENBIYA (https://www.kenbiya.com/)                               |')
print('   |   3 :RAKUMACHI (https://www.rakumachi.jp/)                            |')
time.sleep(0.3)
print('   |   4 :RENGOTAI (https://www.rals.co.jp/invest/)                        |')
print('   +   5 :SBISYUEKI (https://www.re-guide.jp/investment/)                  +')
print('   |                                                                       |')
print('   |                                                                       |')
print('   +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+\n')

'''

site = input('Please Select Target Site from Fig_1... -> ')
while site:
    if site == '2':
        print('2_KENBIYA Scraping Mode is selected.')
    elif site == '1':
        print('1_E-FUDOSAN Scraping Mode is Now under Constrasting... Sorry...')
        print('This program will run at 2_KENBIYA...')
    elif site == '3':
        print('3_RAKUMACHI Scraping Mode is Now under Constrasting... Sorry...')
        print('This program will run at 2_KENBIYA...')
        continue
    elif site == '4':
        print('4_RENGOTAI Scraping Mode is Now under Constrasting... Sorry...')
        print('This program will run at 2_KENBIYA...')
    elif site == '5':
        print('5_SBISYUEKI Scraping Mode is Now under Constrasting... Sorry...')
        print('This program will run at 2_KENBIYA...')
        continue
    else:
        print('Your Input Caractor is Wrong.')
        print('Please Input Correct Number...\n')

'''
'''

print('Importing Modules...')

tsys = random.uniform(1,2)
time.sleep(tsys)
print('Initializing Complete.')

# --- 対象サイトへのログオン処理 ------------------------------------------------- #

print('Start Login Site process ...')

kbyid = input('Enter Target login ID -> ')
kbypw = input('Enter Target logon PW -> ')

import requests
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('mail@gmail.com', 'P@ssw0rd')
r = requests.post(
    url='https://www.kenbiya.com/app/exe/login', auth=auth)
print(r.text)

'''


tsys = random.uniform(1,2)
time.sleep(tsys)
print('Logon Process Faulare...')

# --- ヘッダーの擬態① ------------------------------------------------------------- #

# time.sleep(1.1)
print('Display Header Proccing...')
print('The Generated Header is as follows...\n')
print('   +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+\n')
time.sleep(1.1)

session = requests.Session()
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'\
           'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
           'Accept':'text/html,application/xhtml+xml,application/xml;'\
           'q=0.9,image/webp,*/*;q=0.8'}
url = 'https://www.whatismybrowser.com/'\
'developers/what-http-headers-is-my-browser-sending'
req = session.get(url, headers=headers)
bs = BeautifulSoup(req.text, 'html.parser')
print(bs.find('table',{'class':'table-striped'}).get_text)

# time.sleep(1.3)
print('\n   +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+\n')
print('Header display Complete.')

'''
# --- ヘッダーの擬態② ------------------------------------------------------------- #

ヘッダー予備(cf.p216)
User-Agent:Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X)
AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257
Safari/9537.53

# --- ヘッダーの擬態③ ------------------------------------------------------------- #

session = requests.Session()
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'\
           'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
           'Accept':'text/html,application/xhtml+xml,application/xml;'\
           'q=0.9,image/webp,*/*;q=0.8'}
url = 'https://www.whatismybrowser.com/'\
'developers/what-http-headers-is-my-browser-sending'
req = session.get(url, headers=headers)
bs = BeautifulSoup(req.text, 'html.parser')
print(bs.find('table',{'class':'table-striped'}).get_text)

'''



'''

time.sleep(1.3)
print('Please Enter as follows...\n')

# --- 活動エリアの選択 ------------------------------------------------------------- #


time.sleep(1.3)
print('   +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+')
print('   |                                                                       |')
print('   |   Target Type Menu <Fig_2-1>:                                         |')
print('   |                                                                       |')
print('   +   s :Syutoken                                                         +')
print('   |   k :Kansai                                                           |')
print('   |   t :Tôkai                                                            |')
time.sleep(0.3)
print('   |   f :Kyûsyû/Okinawa                                                   |')
print('   +   h :Hokkaidô,                                                        +')
print('   |   o :Tyugoku/Sikoku                                                   |')
print('   |   z :Sinsyu/Hokuriku                                                  |')
print('   |                                                                       |')
print('   +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+\n')
area = input('Please Select Target Type from Fig_2-1 ... -> ')
tsys = random.uniform(1,2)
time.sleep(tsys)
'''

area = 's'     # あとで消す

'''

# --- 取扱物件の選択 --------------------------------------------------------------- #

print('\n   +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+')
print('   |                                                                       |')
print('   |   <Fig.2-2> Property Type Menu:                                       |')
print('   |                                                                       |')
print('   +    1 :TousiyoumMansion                                                +')
time.sleep(0.1)
print('   |    2 :IttouuriApart                                                   |')
print('   |    3 :IttouuriMaison                                                  |')
print('   |    4 :ItouBil                                                         |')
print('   +    8 :KodateCintai                                                    +')
print('   |   11 :TenpotsukiJyutaku                                               |')
print('   |    9 :Tenpo/Jimusyo                                                   |')
time.sleep(0.2)
print('   |    7 :Koujyou/Souko                                                   |')
print('   +   10 :Hotel                                                           +')
print('   |   12 :Chusyajyo                                                       |')
print('   |    5 :Tochi                                                           |')
print('   |                                                                       |')
print('   +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+\n')
time.sleep(1.1)
tgtt = input('Please Select Property Type from <Fig.2-2>.(cf.1,2,8,12) -> ')
time.sleep(0.5)


bbb = []

aaa = input('input number => ')

bbb.append(aaa)

aaa = input('')

bbb.append(aaa)

aaa = input('')

bbb.append(aaa)

aaa = input('')

bbb.append(aaa)

aaa = input('')

bbb.append(aaa)

aaa = input('')

bbb.append(aaa)

bbb.sort()

print(bbb[0],bbb[1],bbb[2],bbb[3],bbb[4],bbb[5],sep='_')



# --- 続行の可否判断 --------------------------------------------------------------- #

from sys import stdin

print('Initiate Mimicry Access to Target ? (y|n) -> ')
ans = stdin.readline()

if ans.strip() == "n":
    print ('\nMimicryAccess Started...\n')
else:
    print ('\nProgram Aborted...')

ans = input('Start MimicryAccess to Target (y|n) ? -> ')
if ans == 'y':
    print('\nMimicryAccess Started...\n')     # 「y」ならコンテニュー。
    continue
else:
    print('\n<<< Program Aborted. >>>\n')     # 「n」なら中断。
    break

tsys = random.uniform(1,2)
time.sleep(tsys)

'''

'''
# --- ダミーのページ遷移スクリプト ------------------------------------------------- #

time.sleep(0.7)
print('Initiate Pre-Access by Mimicry Mode Prosess.')
time.sleep(0.7)
# print('TargetType is -'+ area + ' and PropertyType is ' + tgtt)
time.sleep(0.7)
print('Please Wait...')
time.sleep(0.7)
print('Initiate Pre-Access by Mimicry Mode on Target Site...\n')
time.sleep(0.7)

print('   +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+\n')

'''
sect = ['s','k','t','f','h','m','o','z']
kyad = 'https://www.kenbiya.com'

'''
html = urlopen(kyad + '')     # ダミー遷移開始、人がリンクを順番に辿っているが如く擬態
tlow = random.uniform(1.1,3.1)
time.sleep(tlow)
print('Mimicry_Mode( 1/13), ' + 'Target_Type:-' + area + ', Delay:' + str(tlow) +  '...')

html = urlopen(kyad + '/pp2/')
tlow = random.uniform(1.1,3.1)
time.sleep(tlow)
print('Mimicry_Mode( 2/13), ' + 'Target_Type:-' + area + ', Delay:' + str(tlow) +  '...')

html = urlopen(kyad + '/pp2_3/')
tlow = random.uniform(1.1,3.1)
time.sleep(tlow)
print('Mimicry_Mode( 3/13), ' + 'Target_Type:-' + area + ', Delay:' + str(tlow) +  '...')

html = urlopen(kyad + '/pp2_3_4/')
tlow = random.uniform(1.1,3.1)
time.sleep(tlow)
print('Mimicry_Mode( 4/13), ' + 'Target_Type:-' + area + ', Delay:' + str(tlow) +  '...')

html = urlopen(kyad + '/pp2_3_4_5/')
tlow = random.uniform(1.1,3.1)
time.sleep(tlow)
print('Mimicry_Mode( 5/13), ' + 'Target_Type:-' + area + ', Delay:' + str(tlow) +  '...')

html = urlopen(kyad + '/pp2_3_4_5_7/')
tlow = random.uniform(1.1,3.1)
time.sleep(tlow)
print('Mimicry_Mode( 6/13), ' + 'Target_Type:-' + area + ', Delay:' + str(tlow) +  '...')

loc = random.choice(sect)
html = urlopen(kyad + '/pp2_3_4_5_7/' + loc)
tlow = random.uniform(1.1,3.1)
time.sleep(tlow)
print('Mimicry_Mode( 7/13), ' + 'Target_Type:-' + loc + ', Delay:' + str(tlow) +  '...')

loc = random.choice(sect)
html = urlopen(kyad + '/pp2_3_4_5_7/' + loc)
thi = random.uniform(5,20)
time.sleep(thi)
print('Mimicry_Mode( 8/13), ' + 'Target_Type:-' + loc + ', Delay:' + str(tlow) +  '...')

loc = random.choice(sect)
html = urlopen(kyad + '/pp2_3_4_5_7/' + loc)
tlow = random.uniform(1.1,3.1)
time.sleep(tlow)
print('Mimicry_Mode( 9/13), ' + 'Target_Type:-' + loc + ', Delay:' + str(tlow) +  '...')

html = urlopen(kyad + '/pp2_3_4_5_7/' + area + '/')
tlow = random.uniform(1.1,3.1)
time.sleep(tlow)
print('Mimicry_Mode(10/13), ' + 'Target_Type:-' + area + ', Delay:' + str(tlow) +  '...')

html = urlopen(kyad + '/pp2_3_4_5_7/' + area + '/n-' + '2' + '/')
thi = random.uniform(5,20)
time.sleep(thi)
print('Mimicry_Mode(11/13), ' + 'Target_Type:-' + area + ', Delay:' + str(tlow) +  '...')

html = urlopen(kyad + '/pp2_3_4_5_7/' + area + '/n-' + '4' + '/')
thi = random.uniform(5,20)
time.sleep(thi)
print('Mimicry_Mode(12/13), ' + 'Target_Type:-' + area + ', Delay:' + str(tlow) +  '...')

html = urlopen(kyad + '/pp2_3_4_5_7/' + area + '/n-' + '3' + '/')     # ダミー遷移完了
time.sleep(random.uniform(5,20))
print('Mimicry_Mode(13/13), ' + 'Target_Type:-' + area + ', Delay:' + str(tlow) +  '...')

print('\n   +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+\n')
print('Access by Mimicry Mode is Succesed.')
'''
'''
# ---リンクを抽出(cf.p34) ---------------------------------------------------------- #

# 続行の可否判断
ans = input('Execute Crawling Target? (y|n) -> ')

if ans == 'y':
    print('\nInitiate Scraping Process...\n')     # 「y」ならコンテニュー。
    continue
else:
    print('\n<<< Program Aborted... >>>\n')     # 「n」なら中断。
    break
'''


# --- 配列の作成 ------------------------------------------------------------------- #

print('Construct a Main Book on Storage...')
# time.sleep(0.6)

scda_copn = []    # 配列の作成（会社名データ格納）
scda_licn = []    # 配列の作成（免許番号データ格納）
scda_zipc = []    # 配列の作成（郵便番号データ格納）
scda_addc = []    # 配列の作成（所在地データ格納）
scda_urlc = []    # 配列の作成（URLデータ格納）
scda_teln = []    # 配列の作成（電話番号データ格納）
scda_faxn = []    # 配列の作成（Fax番号データ格納）
scda_main = [[scda_copn],[scda_licn],[scda_addc],[scda_urlc],[scda_teln],[scda_faxn]]    # メイン台帳の構造を定義
scda_main_a = []
scda_main_b = []
scda_main_c = []
scda_main_d = []
scda_main_e = []
scda_main_f = []
scda_main_g = []

print('Main Book is constructed.')
# time.sleep(0.6)



# --- csvファイルの作成 ------------------------------------------------------------ #

ut = time.time()                                          # ファイル名生成用エポック数の取得
ftime = str(ut)                                           # str型に変換
csvfle = open('CrawingByMsuka_' + ftime + '.csv', 'w+')   # csvファイルの生成
print('CrawingByMsuka_' + str(ut) + '.csv', 'w+')         #ファイル名の表示
writecsv = csv.writer(csvfle, lineterminator = '\n')
writecsv.writerow(('会社名', '免許番号', '所在地', 'URL', '電話番号', 'Fax番号'))     #ここまではＯＫっぽい。



# --- ここまでを組み合わせてスクレイピング ------------------------------------------- #
# csvへのライトに関するコードは、途中でスクリプトが停止してもそこまでのデータは残るよう、ひとまとまりにせず、各for文に入れ込んでいる。

print('\n   +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+\n')
print('Now Scraping on URL: ' + kyad + '/pp2_3_4_5_7/' + area + '/n-100/...')
print('   + - - - - - - - - - - - + - - - - - - - - - - - + - - - - - - - - - - - +')

# html = urlopen(kyad + '/pp2_4_5_7/' + area + '/n-124/') # あとで消す
html = urlopen('https://www.kenbiya.com/pp2_4_5_7/s/n-100/')
thi = random.uniform(1.5,5.5)
time.sleep(thi)
bs = BeautifulSoup(html, 'html.parser')
for link in bs.find_all('a', href=re.compile('^(/pp)(?=.*/re_1).*$')):       # 物件ページへのリンクを正規表現で探索。
    time.sleep(2)
    if 'href' in link.attrs:                                                 # 「link」は変数宣言していないのになぜ動く？予約語なのか？
        time.sleep(random.uniform(1.5,5.5))                                  # 待機
        html = urlopen(kyad + link.attrs['href'])                            # htmlを定義
        bs = BeautifulSoup(html, 'html.parser')                              # bsオブジェクトを作成
        # ------------------------------------------------------------------ #
        copn = bs.find('h4',text=re.compile("株式会社|有限会社|合同会社"))     # 「会社名」の抽出。find_allではなくfindとすることで最初に出現する会社名をスクレイプする。（サイト内のタグに特徴が無いためこの方法しか無い。）
        licn = bs.find_all('p', text=re.compile("大臣|知事"))                # 「免許番号」の抽出。
      # zipc = bs.find_all('p',text=re.compile("〒"))                        # 「所在地」の抽出。
        addc = bs.find_all('p',text=re.compile("都|道|府|県"))                # 「所在地」の抽出。
      # urlc = bs.find_all(text=re.compile("URL："))                         # 「URL」の抽出。
        teln = bs.find_all(text=re.compile("TEL："))                         # 「電話番号」の抽出。
        faxn = bs.find_all(text=re.compile("FAX："))                         # 「Fax番号」の抽出。
        # ------------------------------------------------------------------ #
        for copn in copn:
            tlow = random.uniform(1.1,2.1)
            time.sleep(tlow)
            scda_copn.append(copn.string)                                    # 取得した「copn」データをscdaリストに格納
            print(copn.string)
            '''
        for licn in licn:
            tlow = random.uniform(1.1,2.1)
            time.sleep(tlow)
            scda_licn.append(licn.string)                                    # 取得した「licn」データをscdaリストに格納
            print(licn.string)
            '''
      # for zipc in zipc:
          # tlow = random.uniform(1.1,2.1)
          # time.sleep(tlow)
          # scda_zipc.append(zipc.string)                                    # 取得した「zipc」データをscdaリストに格納
          # print(zipc.string)
        for addc in addc:
            tlow = random.uniform(1.1,2.1)
            time.sleep(tlow)
            scda_addc.append(addc.string)                                    # 取得した「addc」データをscdaリストに格納
            print(addc.string)
      # for urlc in urlc:
          # tlow = random.uniform(1.1,2.1)
          # time.sleep(tlow)
          # scda_urlc.append(urlc.string)                                    # 取得した「urlc」データをscdaリストに格納
          # print(urlc.string)
        for teln in teln:
            tlow = random.uniform(1.1,2.1)
            time.sleep(tlow)
            scda_teln.append(teln.string)                                    # 取得した「teln」データをscdaリストに格納
            print(teln.string)
        for faxn in faxn:
            tlow = random.uniform(1.1,2.1)
            time.sleep(tlow)
            scda_faxn.append(faxn.string)                                    # 取得した「faxn」データをscdaリストに格納
            print(faxn.string)
        for copn in range(1):
            print('   + - - - - - - - - - - - + - - - - - - - - - - - + - - - - - - - - - - - +')
            writecsv.writerow(scda_copn)                                     # 「copn」データをcsv出力
            writecsv.writerow(scda_licn)                                     # 「licn」データをcsv出力
            writecsv.writerow(scda_zipc)                                     # 「zipc」データをcsv出力
            writecsv.writerow(scda_addc)                                     # 「addc」データをcsv出力
            writecsv.writerow(scda_urlc)                                     # 「urlc」データをcsv出力
            writecsv.writerow(scda_teln)                                     # 「teln」データをcsv出力
            writecsv.writerow(scda_faxn)                                     # 「faxn」データをcsv出力
csvfle.close()                                                               # csvファイルを閉じる
print('\nScraping Process Complete.\n')
print('   +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+\n')



# --- 得られた結果を加工(cf.p) ----------------------------------------------------- #






# --- 結果のcsv出力(cf.p86) -------------------------------------------------------- #






'''
scda_main_a.append(scda_copn[0],scda_licn[0],scda_addc[0],scda_urlc[0],scda_teln[0],scda_faxn[0])
scda_main_b.append(scda_copn[1],scda_licn[1],scda_addc[1],scda_urlc[1],scda_teln[1],scda_faxn[1])
scda_main_c.append(scda_copn[2],scda_licn[2],scda_addc[2],scda_urlc[2],scda_teln[2],scda_faxn[2])
scda_main_d.append(scda_copn[3],scda_licn[3],scda_addc[3],scda_urlc[3],scda_teln[3],scda_faxn[3])
scda_main_e.append(scda_copn[4],scda_licn[4],scda_addc[4],scda_urlc[4],scda_teln[4],scda_faxn[4])
scda_main_f.append(scda_copn[5],scda_licn[5],scda_addc[5],scda_urlc[5],scda_teln[5],scda_faxn[5])
scda_main_g.append(scda_copn[6],scda_licn[6],scda_addc[6],scda_urlc[6],scda_teln[6],scda_faxn[6])

'''











'''
# 重複する結果は一つにまとめ、出現回数をカウントする。


print('Now CSV Generating...')
time.sleep(0.6)
print('Please Wait...\n')

csvFile = open('CrawingByMsuka_' + area + '.csv', 'w+')
try:
    writer = csv.writer(csvFile)
    writer.writerow(('','','','','会社名', '免許番号', '所在地', 'URL', '', '', '', '電話番号', 'Fax番号'))     #ここまではＯＫっぽい。
    for copn in copn:
        writer.writerows([copn])
finally:
    csvfile.close()

print('CSV File is Generated.')
time.sleep(0.9)






# アクセスするURL
url = "https://mainichi.jp/"
# URLを開く
html = urllib.request.urlopen(url)
# BeautifulSoupで開く
soup = BeautifulSoup(html, "html.parser")

# HTMLからニュース一覧に使用しているaタグを絞りこんでいく
tag_mainbox = soup.select_one(".main-box")
tag_listA = tag_mainbox.select_one(".list-typeA")
news_tag = tag_listA.findAll("a")






# 配列の作成。
for copn in copn:
    copn = copn.text
    csvlist.append(copn)

# CSVファイルを開く。ファイルがなければ新規作成する。
f = open("output.csv", "w")
writecsv = csv.writer(f, lineterminator='\n')

# 出力
writecsv.writerow(csvlist)

# CSVファイルを閉じる。
f.close()




'''






# --- 終了処理 --------------------------------------------------------------------- #

xxx = input('Exit Crawing Program (y|n)? -> ')
# while (xxx != 'y' and xxx != 'n'):
#    print('Your input carator is incorrect.')
#    print('Please Input y or n.')
if xxx == 'y':
    print('Crawing Program Terminated.')
    os.Program('cls')
elif xxx == 'n':
    print('Return to forward.')
    print('please wait...')
else:
    print('Your input carator is incorrect.')
    print('Please Input y or n.')

# ---------------------------------------------------------------------------------- #

# EOF