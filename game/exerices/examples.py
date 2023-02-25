# 创建一个用于存储外星人的空列表
aliens = []

#创建30个绿色的外星人
for alien_number in range(30):
    if alien_number <=15:
        new_alien = {'color': 'green', 'points': 
                5, 'speed': 'slow'}
        aliens.append(new_alien)
    elif alien_number <=25:
        new_alien = {'color': 'yellow', 'points': 
                10, 'speed': 'medium'}
        aliens.append(new_alien)
    else:
        new_alien = {'color': 'red', 'points': 
                15, 'speed': 'fast'}
        aliens.append(new_alien)

#显示前五个外星人
for alien in aliens[:30]:
    print(alien)


# 显示创建了多少个外星人
print("Total number of aliens: " + str(len(aliens)))


