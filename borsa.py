
import random
# import numpy as np
import yfinance as yf
import pandas as pd
from openpyxl import Workbook, load_workbook




wb = load_workbook("durum1.xlsx")
wss = wb.active
c = wss["C2"].value

hisseKodları=['ACSEL.IS', 'ADEL.IS', 'ADESE.IS', 'AEFES.IS', 'AFYON.IS', 'AGHOL.IS', 'AGYO.IS', 'AKBNK.IS', 'AKCNS.IS', 'AKENR.IS', 'AKFGY.IS', 'AKGRT.IS', 'AKMGY.IS', 'AKSA.IS', 'AKSEN.IS', 'AKSGY.IS', 'AKSUE.IS', 'ALARK.IS', 'ALCAR.IS', 'ALCTL.IS', 'ALGYO.IS', 'ALKA.IS', 'ALKIM.IS', 'ANELE.IS', 'ANHYT.IS', 'ANSGR.IS', 'ARCLK.IS', 'ARENA.IS', 'ARMDA.IS', 'ARSAN.IS', 'ARTI.IS', 'ASELS.IS', 'ASUZU.IS', 'ATAGY.IS', 'ATEKS.IS', 'ATLAS.IS', 'ATSYH.IS', 'AVGYO.IS', 'AVHOL.IS', 'AVISA.IS', 'AVOD.IS', 'AVTUR.IS', 'AYCES.IS', 'AYEN.IS', 'AYES.IS', 'AYGAZ.IS', 'BAGFS.IS', 'BAKAB.IS', 'BALAT.IS', 'BANVT.IS', 'BASCM.IS', 'BERA.IS', 'BEYAZ.IS', 'BFREN.IS', 'BFREN.IS', 'BIMAS.IS', 'BIMAS.IS', 'BIZIM.IS', 'BIZIM.IS', 'BJKAS.IS', 'BJKAS.IS', 'BLCYT.IS', 'BLCYT.IS', 'BNTAS.IS', 'BNTAS.IS', 'BOSSA.IS', 'BOSSA.IS', 'BRISA.IS', 'BRISA.IS', 'BRKO.IS', 'BRKO.IS', 'BRKSN.IS', 'BRKSN.IS', 'BRMEN.IS', 'BRSAN.IS', 'BRYAT.IS', 'BSOKE.IS', 'BTCIM.IS', 'BUCIM.IS', 'BURCE.IS', 'BURVA.IS', 'CASA.IS', 'CCOLA.IS', 'CELHA.IS', 'CEMAS.IS', 'CEMTS.IS', 'CIMSA.IS', 'CLEBI.IS', 'CMBTN.IS', 'CMENT.IS', 'COSMO.IS', 'CRDFA.IS', 'CRFSA.IS', 'CUSAN.IS', 'DAGHL.IS', 'DAGI.IS', 'DARDL.IS', 'DENGE.IS', 'DERIM.IS', 'DESA.IS', 'DESPC.IS', 'DEVA.IS', 'DGATE.IS', 'DGGYO.IS', 'DGKLB.IS', 'DIRIT.IS', 'DITAS.IS', 'DMSAS.IS', 'DOAS.IS', 'DOBUR.IS', 'DOCO.IS', 'DOGUB.IS', 'DOHOL.IS', 'DOKTA.IS', 'DURDO.IS', 'DYOBY.IS', 'DZGYO.IS', 'ECILC.IS', 'ECZYT.IS', 'EDIP.IS', 'EGEEN.IS', 'EGGUB.IS', 'EGPRO.IS', 'EGSER.IS', 'EKGYO.IS', 'EKIZ.IS', 'EMKEL.IS', 'EMNIS.IS', 'ENKAI.IS', 'EPLAS.IS', 'ERBOS.IS', 'EREGL.IS', 'ERSU.IS', 'ESCOM.IS', 'ETILR.IS', 'ETYAT.IS', 'EUHOL.IS', 'EUKYO.IS', 'EUYO.IS', 'FENER.IS', 'FLAP.IS', 'FMIZP.IS', 'FRIGO.IS', 'FROTO.IS', 'GARFA.IS', 'GEDIK.IS', 'GEDZA.IS', 'GENTS.IS', 'GEREL.IS', 'GLRYH.IS', 'GLYHO.IS', 'GOLTS.IS', 'GOODY.IS', 'GOZDE.IS', 'GRNYO.IS', 'GSDDE.IS', 'GSDHO.IS', 'GSRAY.IS', 'GUBRF.IS', 'HATEK.IS', 'HDFGS.IS', 'HEKTS.IS', 'HLGYO.IS', 'HUBVC.IS', 'HURGZ.IS', 'IDEAS.IS', 'IDGYO.IS', 'IEYHO.IS', 'IHEVA.IS', 'IHGZT.IS', 'IHLAS.IS', 'IHLGM.IS', 'IHYAY.IS', 'INDES.IS', 'INTEM.IS', 'INVEO.IS', 'IPEKE.IS', 'ISBIR.IS', 'ISDMR.IS', 'ISFIN.IS', 'ISGYO.IS', 'ISYAT.IS', 'ITTFH.IS', 'IZFAS.IS', 'IZMDC.IS', 'IZTAR.IS', 'JANTS.IS', 'KAPLM.IS', 'KAREL.IS', 'KARSN.IS', 'KARTN.IS', 'KATMR.IS', 'KCHOL.IS', 'KENT.IS', 'KERVN.IS', 'KERVT.IS', 'KLGYO.IS', 'KLMSN.IS', 'KNFRT.IS', 'KONYA.IS', 'KORDS.IS', 'KOZAA.IS', 'KOZAL.IS', 'KRGYO.IS', 'KRONT.IS', 'KRSTL.IS', 'KRTEK.IS', 'KUTPO.IS', 'KUYAS.IS', 'LIDFA.IS', 'LINK.IS', 'LKMNH.IS', 'LOGO.IS', 'LUKSK.IS', 'MAALT.IS', 'MAKTK.IS', 'MARKA.IS', 'MARTI.IS', 'MAVI.IS', 'MEGAP.IS', 'MEPET.IS', 'MERIT.IS', 'MERKO.IS', 'METRO.IS', 'METUR.IS', 'MGROS.IS', 'MIPAZ.IS', 'MMCAS.IS', 'MNDRS.IS', 'MRGYO.IS', 'MRSHL.IS', 'MSGYO.IS', 'MTRYO.IS', 'MZHLD.IS', 'NETAS.IS', 'NIBAS.IS', 'NTHOL.IS', 'NUGYO.IS', 'NUHCM.IS', 'ODAS.IS', 'OLMIP.IS', 'ORGE.IS', 'ORMA.IS', 'OSTIM.IS', 'OTKAR.IS', 'OYAKC.IS', 'OYAYO.IS', 'OYLUM.IS', 'OZBAL.IS', 'OZGYO.IS', 'OZKGY.IS', 'OZRDN.IS', 'PAGYO.IS', 'PARSN.IS', 'PEGYO.IS', 'PENGD.IS', 'PETKM.IS', 'PETUN.IS', 'PGSUS.IS', 'PINSU.IS', 'PKART.IS', 'PKENT.IS', 'PNSUT.IS', 'POLHO.IS', 'POLTK.IS', 'PRKAB.IS', 'PRKME.IS', 'PRZMA.IS', 'PSDTC.IS', 'QNBFL.IS', 'RALYH.IS', 'RAYSG.IS', 'RHEAG.IS', 'RODRG.IS', 'ROYAL.IS', 'RTALB.IS', 'RYGYO.IS', 'RYSAS.IS', 'SAHOL.IS', 'SAMAT.IS', 'SANEL.IS', 'SANFM.IS', 'SANKO.IS', 'SARKY.IS', 'SASA.IS', 'SAYAS.IS', 'SEKFK.IS', 'SEKUR.IS', 'SELEC.IS', 'SELGD.IS', 'SERVE.IS', 'SEYKM.IS', 'SILVR.IS', 'SISE.IS', 'SKTAS.IS', 'SNGYO.IS', 'SNKRN.IS', 'SNPAM.IS', 'SODSN.IS', 'SONME.IS', 'SRVGY.IS', 'TACTR.IS', 'TATGD.IS', 'TAVHL.IS', 'TBORG.IS', 'TCELL.IS', 'TEKTU.IS', 'TGSAS.IS', 'THYAO.IS', 'TIRE.IS', 'TKFEN.IS', 'TKNSA.IS', 'TKURU.IS', 'TMPOL.IS', 'TMSN.IS', 'TOASO.IS', 'TRCAS.IS', 'TRGYO.IS', 'TSGYO.IS', 'TSPOR.IS', 'TTKOM.IS', 'TTRAK.IS', 'TUCLK.IS', 'TUKAS.IS', 'TUPRS.IS', 'TURGG.IS', 'TURSG.IS', 'UFUK.IS', 'ULAS.IS', 'ULKER.IS', 'ULUSE.IS', 'ULUUN.IS', 'UMPAS.IS', 'USAK.IS', 'UTPYA.IS', 'UZERB.IS', 'VAKFN.IS', 'VAKKO.IS', 'VANGD.IS', 'VERTU.IS', 'VERUS.IS', 'VESBE.IS', 'VESTL.IS', 'VKFYO.IS', 'VKGYO.IS', 'VKING.IS', 'YAPRK.IS', 'YATAS.IS']
tickers = []
maliyet=[]
kazanç=[]
ana_para=10000

def random_fibonaci():

    for i in range(3):

        new=random.sample(hisseKodları,348)
        fibon=[0,1,2,3,5,8,13,21,34,55,89,144,233]
        for i in range(13):
            tickers.append(new[fibon[i]])
    new2=random.sample(tickers,30)
    return new2


tickers=random_fibonaci()

start = '2021-11-20'
end = '2021-12-20'

def tarih(start=start,end=end):
    start1=start
    end1=end
    return start1,end1   


# tickers = ['ACSEL.IS', 'ADEL.IS', 'ADESE.IS', 'AEFES.IS']




# Hisse senetleri verilerini indir
portfolio_data = yf.download(tickers, start=tarih()[0], end=tarih()[1])

# portfolio_data.iloc[i] * pd.Series([100, 100, 100, 100])
sayı=len(tickers[0])

# Portföyün her gün için performansını hesapla
for i in range(portfolio_data.shape[0]):
    date = portfolio_data.index[i]
    initial_value = (portfolio_data.iloc[0].reset_index(drop=True) * pd.Series([100]*sayı)).sum()
    final_value = (portfolio_data.iloc[i].reset_index(drop=True) * pd.Series([100]*sayı)).sum()

    profit_loss = final_value - initial_value
    performance = (final_value - initial_value) / initial_value * 100
    # print(f'{date}: Performans: {performance:.2f}%, Kar/Zarar: {profit_loss:.2f}')

            
date1=0

initial_value = (portfolio_data.iloc[0].reset_index(drop=True) * pd.Series([100]*sayı)).sum()
target_value = initial_value + (initial_value * 0.15)
for i in range(portfolio_data.shape[0]):
    date = portfolio_data.index[i]
    final_value = (portfolio_data.iloc[i].reset_index(drop=True) * pd.Series([100]*sayı)).sum()
    if final_value >= target_value:
        performance = (final_value - initial_value) / initial_value * 100
        
        
        x=(f'Portföy {performance:.2f}% kar etti: {date}')
        print(x)
        date1= date.to_pydatetime().date()  
        break


# def run():
#     # Fonksiyon içeriği
#     date2=date1
#     return date2
    

# def get_tickers_from_istanbul_stock_exchange():
#     isx = yf.Ticker("^XUTUM")
#     isx_info = isx.info
#     tickers = isx_info["components"]
#     return [ticker["symbol"] for ticker in tickers]

# tickerss = get_tickers_from_istanbul_stock_exchange()
# print(tickerss)
