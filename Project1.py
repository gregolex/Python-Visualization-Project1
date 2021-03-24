from pandas import Series, DataFrame as df
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

DataFrame1 = pd.read_csv("NYC Leading Causes of Death.csv")
deathsIn2014 = DataFrame1.loc[4:139, ['Deaths']]
deathsIn2013 = DataFrame1.loc[140:272, ['Deaths']]
deathsIn2012 = DataFrame1.loc[273:406, ['Deaths']]
deathsIn2011 = DataFrame1.loc[407:547, ['Deaths']]
deathsIn2010 = DataFrame1.loc[548:685, ['Deaths']]
deathsIn2009 = DataFrame1.loc[686:820, ['Deaths']]
deathsIn2008 = DataFrame1.loc[821:956, ['Deaths']]
deathsIn2007 = DataFrame1.loc[957:1094, ['Deaths']]
AllDeaths = DataFrame1.loc[1:1094, ['Deaths']]
MaleAttributes = DataFrame1[DataFrame1['Sex'].str.match('Male')]
FemaleAttributes = DataFrame1[DataFrame1['Sex'].str.match('Female')]
MaleDeaths = MaleAttributes.loc[1:1094, ['Deaths']]
FemaleDeaths = FemaleAttributes.loc[1:1094, ['Deaths']]
DeathRate = DataFrame1.loc[1:1094, ['DeathRate']]
AADeathRate = DataFrame1.loc[1:1094, ['AgeAdjustedDeathRate']]
deathsIn2007.apply(pd.to_numeric)
AllDeaths = AllDeaths.apply(pd.to_numeric)
MaleDeaths = MaleDeaths.apply(pd.to_numeric)
DeathRate = DeathRate.apply(pd.to_numeric)
AADeathRate = AADeathRate.apply(pd.to_numeric)

ser1 = pd.Series(DataFrame1['AgeAdjustedDeathRate'])
ser2 = pd.Series(DataFrame1['DeathRate'])



AgeAdjustedDeathRateMean = np.mean(ser1)
DeathRateMean = np.mean(ser2)

print(DeathRateMean)
print(AgeAdjustedDeathRateMean)

sns.violinplot(x = "Deaths", data=deathsIn2007)
plt.show()

sns.violinplot(x = "Deaths", data=DataFrame1)
plt.show()

AllDeaths = AllDeaths.cumsum()
plt.figure()
AllDeaths.plot()


deathsIn2014a = deathsIn2014.cumsum()
plt.figure()
deathsIn2014a.plot()


deathsIn2014b = deathsIn2014.plot.line()

DeathRateA = DeathRate.cumsum()
DeathRateA.plot.bar()

AADeathRateA = AADeathRate.cumsum()
AADeathRateA.plot.line()

AADeathRateA = AADeathRate.cumsum()
AADeathRateA.plot.bar()

MaleDeathsA = MaleDeaths.cumsum()
plt.figure()
MaleDeathsA.plot(kind='box', stacked=True)

FemaleDeathsA = FemaleDeaths.cumsum()
plt.figure()
FemaleDeathsA.plot(kind='box', stacked=True)

result = pd.concat([MaleDeathsA, FemaleDeathsA], axis=0, sort=True)
result.boxplot(column=["Deaths", "Deaths"])

