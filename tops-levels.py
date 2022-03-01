//@version=4

study(title="Tops Levels", shorttitle="Tops Levels", overlay=true)

// Intraday High & Low
dailyhigh = security(syminfo.tickerid, 'D', high)
dailylow = security(syminfo.tickerid, 'D', low)

// Previous Day High & Low
previousdayhigh = security(syminfo.tickerid, 'D', high[1])
previousdaylow = security(syminfo.tickerid, 'D', low[1])

// Pre-Market High & Low
t = time("1440","0400-0930") // 1440 is the number of minutes in a whole day.
is_first = na(t[1]) and not na(t) or t[1] < t
ending_hour = 9
ending_minute = 30

pm_high = float(na)
pm_low = float(na)
k = int(na)

if is_first and barstate.isnew and ((hour < ending_hour or hour >= 16) or (hour == ending_hour and minute < ending_minute))
    pm_high := high
    pm_low := low
else 
    pm_high := pm_high[1]
    pm_low := pm_low[1]

if high > pm_high and ((hour < ending_hour or hour >= 1600) or (hour == ending_hour and minute < ending_minute))
    pm_high := high
    
if low < pm_low and ((hour < ending_hour or hour >= 1600) or (hour == ending_hour and minute < ending_minute))
    pm_low := low

LastOnly = true

if LastOnly==true
    k:=-9999
else
    k:=0
    
    //After Hours High & Low
ti = time("1440","1600-2000") // 1440 is the number of minutes in a whole day.
is_first1 = na(ti[1]) and not na(ti) or ti[1] < ti
ending_hour1 = 20
ending_minute1 = 00

ah_high = float(na)
ah_low = float(na)
g = int(na)

if is_first1 and barstate.isnew and ((hour < ending_hour1 or hour >= 20) or (hour == ending_hour1 and minute < ending_minute1))
    ah_high := high
    ah_low := low
else 
    ah_high := ah_high[1]
    ah_low := ah_low[1]

if high > ah_high and ((hour < ending_hour1 or hour >= 2000) or (hour == ending_hour1 and minute < ending_minute1))
    ah_high := high
    
if low < ah_low and ((hour < ending_hour1 or hour >= 2000) or (hour == ending_hour1 and minute < ending_minute1))
    ah_low := low

LastOnly1 = true

if LastOnly1==true
    g:=-9999
else
    g:=0

//Just a variable here for the label coordinates
td = time - time[5]

// Intraday High & Low
plot(dailyhigh, style=plot.style_line,title="Intraday High", color=#ffffff, linewidth=2, trackprice=true,offset=k)
dh = label.new(x=time+td, y=dailyhigh, text = "Today's High", xloc = xloc.bar_time, style = label.style_none, textcolor = #ffffff, size = size.normal, textalign = text.align_right)
label.delete(dh[1])

plot(dailylow, style=plot.style_line,title="Intraday Low",color=#ffffff, linewidth=2, trackprice=true,offset=k)
dl = label.new(x=time+td, y=dailylow, text = "Today's Low", xloc = xloc.bar_time, style = label.style_none, textcolor = #ffffff, size = size.normal, textalign = text.align_right)
label.delete(dl[1])

// Previous Day High & Low
plot(previousdayhigh, style=plot.style_line,title="Yesterday's High",color=#6385FF, linewidth=2, trackprice=true,offset=k)
pdh = label.new(x=time+td, y=previousdayhigh, text = "Yesterday's High", xloc = xloc.bar_time, style = label.style_none, textcolor = #6385FF, size = size.normal, textalign = text.align_right)
label.delete(pdh[1])

plot(previousdaylow, style=plot.style_line,title="Yesterday's Low",color=#6385FF, linewidth=2, trackprice=true,offset=k)
pdl = label.new(x=time+td, y=previousdaylow, text = "Yesterday's Low", xloc = xloc.bar_time, style = label.style_none, textcolor = #6385FF, size = size.normal, textalign = text.align_right)
label.delete(pdl[1])

// Pre-Market High & Low
plot(pm_high, style=plot.style_line,title="Pre-Market High", trackprice=true, color=#FFCF4A, linewidth=2,offset=k)
pmh = label.new(x=time+td, y=pm_high, text = "Pre-Market High", xloc = xloc.bar_time, style = label.style_none, textcolor = #FFCF4A, size = size.normal, textalign = text.align_right)
label.delete(pmh[1])

plot(pm_low, style=plot.style_line,title="Pre-Market Low", trackprice=true, color=#FFCF4A, linewidth=2,offset=k)
pml = label.new(x=time+td, y=pm_low, text = "Pre-Market Low", xloc = xloc.bar_time, style = label.style_none, textcolor = #FFCF4A, size = size.normal, textalign = text.align_right)
label.delete(pml[1])
