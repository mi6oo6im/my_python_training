# При скорост до 10 (включително) отпечатайте &quot;slow&quot;
#  При скорост над 10 и до 50 (включително) отпечатайте &quot;average&quot;
#  При скорост над 50 и до 150 (включително) отпечатайте &quot;fast&quot;
#  При скорост над 150 и до 1000 (включително) отпечатайте &quot;ultra fast&quot;
#  При по-висока скорост отпечатайте &quot;extremely fast&quot;

speed = float(input())
if speed <= 10:
    print('slow')
elif 10 < speed <= 50:
    print('average')
elif 50 < speed <= 150:
    print('fast')
elif 150 < speed <= 1000:
    print('ultra fast')
else:
    print('extremely fast')
