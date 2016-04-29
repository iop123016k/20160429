
# coding: utf-8

# In[1]:

joke = {
    "學生": "老師我拉肚子了",
    "老師": "你就不能說的文雅點嗎?",
    "學生": "老師我菊部有降雨",
    "老師": "......",
    }
x = "學生"
print(x, "say:", joke[x])


# In[2]:

a=7


# In[3]:

a=7
print(a)


# In[4]:

type(a)


# In[5]:

type(b)


# In[6]:

b=a


# In[7]:

print(b)


# In[8]:

type(b)


# In[9]:

+123


# In[10]:

-123


# In[11]:

9/5


# In[12]:

9//5


# In[13]:

5/0


# In[14]:

a=95
a


# In[15]:

a-3


# In[16]:

a


# In[17]:

a=a-3


# In[18]:

a


# In[19]:

a=a-3
a


# In[20]:

a=95
a-=3
a


# In[21]:

a=95
a=a-3
a


# In[22]:

a=92
a=a+8
a


# In[23]:

a=92
a+=8
a


# In[24]:

a=100
a*=2
a


# In[25]:

a=100
a=a*2
a


# In[26]:

a=200
a/=3
a


# In[27]:

a=13
a//=4
a


# In[28]:

9%5


# In[29]:

divmod(9,5)


# In[30]:

9//5


# In[31]:

9%5


# In[32]:

2+3*4


# In[33]:

2+(3*4)


# In[34]:

10


# In[35]:

0b10


# In[36]:

0o10


# In[37]:

0*10


# In[38]:

0x10


# In[39]:

int(True)


# In[40]:

int(False)


# In[41]:

int(98.6)


# In[42]:

int(1.0e4)


# In[43]:

int(-23)


# In[44]:

int(+23)


# In[45]:

int('99 beer')


# In[46]:

int('98.6')


# In[47]:

int('98.6')


# In[48]:

googol=10**100


# In[49]:

googol


# In[50]:

googol*googol


# In[51]:

float(True)


# In[52]:

float(False)


# In[53]:

float(98)


# In[54]:

float(99)


# In[55]:

float(1.04e4)


# In[56]:

'Snap'


# In[57]:

"Snap"


# In[58]:

"'您好,'xx個人電腦維修工作室"


# In[59]:

"您好,xx個人電腦維修工作室"


# In[60]:

"""中文測試"""


# In[61]:

'''中文'''


# In[62]:

joke = '''有一天
明明:我爸爸在公車上會讓人,你爸爸會嗎?
笑笑:不會.
明明:為什麼?
笑笑:因為,他是公車師機.'''
print(joke)


# In[63]:

'有一天\n明明:我爸爸在公車上會讓人,你爸爸會嗎?\n笑笑:不會.\n明明:為什麼?\n笑笑:因為,他是公車師機.'


# In[64]:

bottles=99
base=''
base+='現有存量'
base+=str(bottles)
base


# In[65]:

str(98.6)


# In[66]:

str(1.0e4)


# In[67]:

joke = '有一天\n明明:我爸爸在公車上會讓人,你爸爸會嗎?\n笑笑:不會.\n明明:為什麼?\n笑笑:因為,他是公車師機.'
print(joke)


# In[68]:

print('\tabc')


# In[69]:

print('a\tbc')


# In[70]:

print('ab\tc')


# In[71]:

joke="中文的\"


# In[72]:

joke="中文的\"示範\""
print(joke)


# In[73]:

"有一天"+",媽媽回家很累"


# In[74]:

print("有一天"+",媽媽回家很累")


# In[75]:

a="生日快樂!"
b="生日快樂!"
c="朋友!"
print(a,b,c)


# In[76]:

Start='開始'*3+'\n'
Middle='中間'*4+'\n'
End='結尾'
print(Start+Start+Middle+End)


# In[77]:


joke = '''小明在睡覺被弟弟吵醒
小明：弟弟我不是告訴你在吵我會好好修理你。
弟弟：哥哥我就是想要讓你修理我把我修成機器人。
小明不想理...'''
print(joke)


# In[78]:

print(joke[0:30])


# In[79]:

name="jerry"
name[0]="H"


# In[80]:

name.replace('j','H')


# In[81]:

joke = '''小明在睡覺被弟弟吵醒
小明：弟弟我不是告訴你在吵我會好好修理你。
弟弟：哥哥我就是想要讓你修理我把我修成機器人。
小明不想理...'''
joke[:]


# In[82]:

print(joke[20:])


# In[83]:

print(joke[12:15])


# In[84]:

print(joke[-4])


# In[85]:

print(joke[18:-2])


# In[86]:

print(joke[::7])


# In[87]:

print(joke[4:20:3])


# In[88]:

len(joke)


# In[89]:


joke2 = '''香蕉對蘋果說：我是個厲害的香蕉。
蘋果：你哪裡厲害只能給人吃？
香蕉：嘿嘿～我可以讓人摔得四腳朝天。
蘋果：.........."'''
print(joke2)


# In[90]:

joke2.split('')


# In[91]:

joke2 = '''香蕉對蘋果說：我是個厲害的香蕉。
蘋果：你哪裡厲害只能給人吃？
香蕉：嘿嘿～我可以讓人摔得四腳朝天。
蘋果：.........."'''
print(joke2)


# In[92]:

joke2.split(' ')


# In[93]:

joke2.split()


# In[94]:

joke3=['不潮','不用','花錢']
joke3_join=','.join(joke3)
print('提示:',joke3_join)


# In[95]:

joke4='''圈圈圓圓圈圈,天天年年天天的我,深深看你的臉。
生氣的溫柔,埋怨的溫柔的臉'''
print(joke4)


# In[96]:

joke4[:2]


# In[97]:

len(joke4)


# In[98]:

joke4.startwith('圈圈')


# In[99]:

joke4.startswith('圈圈')


# In[100]:

joke4.endswith('的臉')


# In[101]:

word='溫柔'
joke4.find(word)


# In[102]:

joke4[11:20]


# In[103]:

joke4.rfind(word)


# In[104]:

joke4.count(word)


# In[106]:

import requests
reponse=requests.get("http://www.novelscape.net/wxxs/j/jingyong/ffwz/001.htm")
response.encoding="big5"
book1=response.text


# In[ ]:

word2="他"
book1.count(word2)


# In[107]:

import requests
response=requests.get("http://www.novelscape.net/wxxs/j/jingyong/ffwz/001.htm")
response.encoding="big5"
book1=response.text


# In[ ]:

word2="他"
book1.count(word2)


# In[108]:

book1='cooking or cookery is the art of preparing food for consuption with the use of heat...'
book1.strip('.')


# In[109]:

book1.capitalize()


# In[110]:

book1.title()


# In[111]:

book1.upper()


# In[112]:

book1.lower()


# In[113]:

book1.swapcase()


# In[114]:

book1.center(100)


# In[115]:

book1.ljust(100)


# In[116]:

book1.rjust(100)


# In[117]:

book1.replace('cooking','煮飯')


# In[118]:

book1.replace('of','的')


# In[ ]:



