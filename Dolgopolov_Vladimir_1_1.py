duration = int(input())
days = duration // (60*60*24)
hours = (duration - days * (60*60*24)) // 3600
minutes = (duration - days * (60*60*24) - hours * 3600) // 60
seconds = duration - days * (60*60*24) - hours * 3600 - minutes * 60
if days > 0:
  print(f'{days} дн {hours} ч {minutes} мин {seconds} сек')
elif days <= 0 and hours > 0:
  print(f'{hours} чаc {minutes} мин {seconds} сек')
elif days <= 0 and hours < 0:
  print(f'{minutes} мин {seconds} сек')
else:
  print(f'{seconds} сек')

# input_seconds = int(input('Введите время в секундах: '))
# days = input_seconds // 86400
# hours = input_seconds // 3600
# minutes = input_seconds // 60 % 60
# seconds = input_seconds % 60
#
# if input_seconds <= 59:
#     print(f'{input_seconds} сек')
# elif input_seconds <= 3599:
#     print(f'{minutes} мин {seconds} сек')
# elif input_seconds <= 86399:
#     print(f'{hours} ч {minutes} мин {seconds} сек')
# else:
#     print(f'{days} дн {hours} ч {minutes} мин {seconds} сек')