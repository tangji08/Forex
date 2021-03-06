# -*- coding:utf-8 -*-
__author__ = 'Jojo'
from Hurst import *
from Indicator import *
import changetime


type = "XAUUSD"
startime = "20070703"
endtime = "20070720"

# for year in range(2001, 2016):
#     filename = type + "_" + str(year) + ".txt"
#     if os.path.exists(datapath + "UTC" + filename):
#         continue
#     Date, Time, Price = changetime.file2data(filename)
#     changetime.writeUTC(Date, Time, Price, datapath + "UTC" + filename)
#
# plotprice_hurst("UTC" + type[-6:], "20080730", "20080803", 50)

# saveBOLL("UTCXAUUSD", "20050304", "20060609", "300")

# plotprice_hurst3("UTCXAUUSD", "20050307", "20050310", 50)


def plotchart(charttype, forextype, startime, endtime, Period):
    if charttype == "Price":
        plotpricechart(forextype, startime, endtime)
    if charttype == "Hurst":
        plotprice_hurst(forextype, startime, endtime, Period)
    if charttype == "MVA":
        plotMVA(forextype, startime, endtime, Period)
    if charttype == "BOLL":
        plotBOLL(forextype, startime, endtime, Period)
