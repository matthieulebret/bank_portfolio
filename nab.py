import streamlit as st

import altair as alt
import plotly.express as px
import matplotlib.pyplot as plt

from cleantext import clean

import numpy as np
import pandas as pd
import datetime
import xlrd

from datetime import datetime
from dateutil.relativedelta import relativedelta

import html2text

import json
import lxml
import openpyxl

# from st_aggrid import AgGrid


st.set_page_config('NAB deals',layout='wide')

st.title('NAB project finance deals')

### Infralogic data

# #
#
# id = [data['transactions'][i]['details']['id'] if not None else 'N/A' for i in range(496)]
# name = [data['transactions'][i]['details']['name'] if not None else 'N/A' for i in range(496)]
# region = [data['transactions'][i]['details']['regions'][0] if not None else 'N/A' for i in range(496)]
# sector = [data['transactions'][i]['details']['sectors'][0] if not None else 'N/A' for i in range(496)]
# currency = [data['transactions'][i]['details']['currency'] if not None else 'N/A' for i in range(496)]
# fundings = [data['transactions'][i]['details']['fundings'] if not None else 'N/A' for i in range(496)]
# countries = [data['transactions'][i]['details']['countries'][0]['name'] if not None else 'N/A' for i in range(496)]
# states = [data['transactions'][i]['details']['countries'][0]['states'] if not None else 'N/A' for i in range(496)]
# subsectors = [data['transactions'][i]['details']['subSectors'][0] if not None else 'N/A' for i in range(496)]
# description = [data['transactions'][i]['details']['description'] if not None else 'N/A' for i in range(496)]
# ratios = [data['transactions'][i]['details']['financeRatios'] if not None else 'N/A' for i in range(496)]
# dominantregion = [data['transactions'][i]['details']['dominantRegion'] if not None else 'N/A' for i in range(496)]
# dominantsector = [data['transactions'][i]['details']['dominantSector'] if not None else 'N/A' for i in range(496)]
# dominantcountry = [data['transactions'][i]['details']['dominantCountry'] if not None else 'N/A' for i in range(496)]
# transactiontype = [data['transactions'][i]['details']['transactionType'] if not None else 'N/A' for i in range(496)]
# dominantsubsector = [data['transactions'][i]['details']['dominantSubSector'] if not None else 'N/A' for i in range(496)]
# transactionstatus = [data['transactions'][i]['details']['transactionLifecycle']['transactionStatus'] if not None else 'N/A' for i in range(496)]
# transactioncharacteristicsPPP = [data['transactions'][i]['details']['transactionCharacteristics']['PPP'] if not None else 'N/A' for i in range(496)]
# transactioncharacteristicsutility = [data['transactions'][i]['details']['transactionCharacteristics']['utility'] if not None else 'N/A' for i in range(496)]
#
# dealdict = {'id':id,'Name':name,'region':region,'sector':sector,'currency':currency,'fundings':fundings,'countries':countries,'states':states,'subsectors':subsectors,
#     'description':description,'ratios':ratios,'dominantRegion':dominantregion,'dominantsector':dominantsector,'dominantcountry':dominantcountry,
#     'transactiontype':transactiontype,'dominantsubsector':dominantsubsector,'transactionstatus':transactionstatus,
#     'PPP':transactioncharacteristicsPPP,'Utility':transactioncharacteristicsutility}
#
# dealdf = pd.DataFrame(dealdict)
#
#
# # df.to_excel('NAB deals.xlsx')
#
# name = []
# type = []
# tenor = []
# amount = []
# role = []
# lenders = []
# dateadded = []
# allocation = []
# estimatedAlloc = []
# estimatedAllocUSD = []
#
# ratings = []
# retired = []
# borrower = []
# comments = []
# monoline = []
# debtclass = []
# margininfo = []
# marginvalue = []
# facilitytype = []
# maturity = []
# lifecyclepoint = []
# amountusd = []
#
#
# for transaction in data['transactions']:
#     for tranche in transaction['details']['fundings']:
#         try:
#             for lender in tranche['lenders']:
#                 try:
#                     name.append(transaction['details']['name'])
#                 except:
#                     name.append(None)
#                 try:
#                     type.append(tranche['type'])
#                 except:
#                     type.append(None)
#                 try:
#                     tenor.append(tranche['tenor'])
#                 except:
#                     tenor.append(None)
#                 try:
#                     amount.append(tranche['amount'])
#                 except:
#                     amount.append(None)
#                 try:
#                     role.append(lender['role'])
#                 except:
#                     role.append(None)
#                 try:
#                     lenders.append(lender['lender']['name'])
#                 except:
#                     lenders.append(None)
#                 try:
#                     dateadded.append(lender['dateAdded'])
#                 except:
#                     dateadded.append(None)
#                 try:
#                     allocation.append(lender['allocation'])
#                 except:
#                     allocation.append(None)
#                 try:
#                     estimatedAlloc.append(lender['estimatedAllocation'])
#                 except:
#                     estimatedAlloc.append(None)
#                 try:
#                     estimatedAllocUSD.append(lender['estimatedAllocationUSD'])
#                 except:
#                     estimatedAllocUSD.append(None)
#                 try:
#                     ratings.append(tranche['ratings'])
#                 except:
#                     ratings.append(None)
#                 try:
#                     borrower.append(tranche['borrower'])
#                 except:
#                     borrower.append(None)
#                 try:
#                     comments.append(tranche['comments'])
#                 except:
#                     comments.append(None)
#                 try:
#                     monoline.append(tranche['monoline'])
#                 except:
#                     monoline.append(None)
#                 try:
#                     debtclass.append(tranche['debtClass'])
#                 except:
#                     debtclass.append(None)
#                 try:
#                     margininfo.append(tranche['marginInfo'])
#                 except:
#                     margininfo.append(None)
#                 try:
#                     marginvalue.append(tranche['marginValue'])
#                 except:
#                     marginvalue.append(None)
#                 try:
#                     facilitytype.append(tranche['facilityType'])
#                 except:
#                     facilitytype.append(None)
#                 try:
#                     maturity.append(tranche['maturityDate'])
#                 except:
#                     maturity.append(None)
#                 try:
#                     lifecyclepoint.append(tranche['lifeCyclePoint'])
#                 except:
#                     lifecyclepoint.append(None)
#                 try:
#                     amountusd.append(tranche['amountUSD'])
#                 except:
#                     amountusd.append(None)
#         except:
#             pass
#
# ticketdf = pd.DataFrame([name,type,tenor,amount,role,lenders,dateadded,allocation,estimatedAlloc, estimatedAllocUSD,ratings,retired,borrower,comments,monoline,debtclass,margininfo,marginvalue,facilitytype,maturity,lifecyclepoint,amountusd]).transpose()
# ticketdf.columns = ['Name','Type','Tenor','Amount','Role','Lender','Date added','Allocation','Estimated Allocation','Estimated Allocation USD','Ratings','Retired','Borrower','Comments','Monoline','Debt Class','Margin info','Margin value','Facility type','Maturity','Life cycle point','Amount USD']
#
#
# bigdf = pd.merge(dealdf,ticketdf,on='Name')
# bigdf.drop('fundings',axis=1,inplace=True)
#
# bigdf.to_excel('nab_deals.xlsx')

def getyear(string,dateadd):
    if string[-1]==')':
        string = string[-5:-1]
    else:
        string = string[-4:]
    try:
        string = int(string)
    except:
        string = dateadd.year
    return string

def getfx(a,b):
    if b == 0:
        return 0
    else:
        return a/b


@st.cache(suppress_st_warning=True)
def getdata():
    df = pd.read_excel('nab_deals.xlsx').iloc[:,1:]
    df['Date added'] = pd.to_datetime(df['Date added'],errors='coerce')
    df['Year'] = df.apply(lambda x:getyear(x['Name'],x['Date added']),axis=1)
    df=df[df['transactionstatus']=='Financial Close']
    df['Allocation'] = pd.to_numeric(df['Allocation'],errors='coerce')
    df['Allocation'] = df['Allocation'].fillna(0)
    df['Estimated Allocation'] = pd.to_numeric(df['Estimated Allocation'],errors='coerce')
    df['Estimated Allocation'] = df['Estimated Allocation'].fillna(0)
    df['Estimated Allocation USD'] = pd.to_numeric(df['Estimated Allocation USD'],errors='coerce')
    df['Estimated Allocation USD'] = df['Estimated Allocation USD'].fillna(0)
    df['Alloc Cur'] = df[['Allocation','Estimated Allocation']].max(axis=1)
    df['Amount'] = pd.to_numeric(df['Amount'],errors='coerce')
    df['Amount'] = df['Amount'].fillna(0)
    df['Amount USD'] = pd.to_numeric(df['Amount USD'],errors='coerce')
    df['Amount USD'] = df['Amount USD'].fillna(0)
    df['Fx'] = df.apply(lambda x: getfx(x['Amount'],x['Amount USD']),axis=1)
    df['Alloc in USD theo'] = df.apply(lambda x:getfx(x['Alloc Cur'],x['Fx']),axis=1)
    df['Ticket USD'] = df[['Estimated Allocation USD','Alloc in USD theo']].max(axis=1)

    return df

df = getdata()


minyear = int(df['Year'].min())
maxyear = int(df['Year'].max())
regions = df['dominantRegion'].unique().tolist()
sectors = df['sector'].unique().tolist()
sectors.insert(0,'All')


yearselect = st.slider('Select period',minyear,maxyear,(2017,maxyear))
df = df[(df['Year']>=yearselect[0])&(df['Year']<=yearselect[1])]

nab = df[df['Lender'].str.contains('National Australia Bank')]

with st.expander('Show data'):
    nab

fig = px.treemap(nab,path=['region','countries','sector','subsectors','Name'],values='Ticket USD',color='region')
st.plotly_chart(fig)

with st.form('my_form'):
    regionselect = st.multiselect('Select regions',regions,['Australasia','Asia'])
    sectorselect = st.selectbox('Select sector',sectors,0)
    st.form_submit_button('Submit')

if sectorselect != 'All':
    df = df[df['sector']==sectorselect]

df = df[df['dominantRegion'].isin(regionselect)]

st.subheader('Partner banks')
banks = pd.DataFrame(df['Lender'].value_counts()/df['Lender'].value_counts().max())
st.write(banks['Lender'].iloc[1:])
