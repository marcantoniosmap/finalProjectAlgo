from random import shuffle
#import re

# start = 0
# end = 10

# def getLorem():
#     str =  "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent non mi ut erat tincidunt placerat. Nam a enim semper, mattis mauris eget, mattis orci. Sed consequat nisi quis orci varius aliquam. Vestibulum a sem vitae nisl maximus porta. Duis blandit enim sed lorem placerat, eget sollicitudin lectus pellentesque. Etiam gravida non massa tristique ultrices. In hac habitasse platea dictumst. Suspendisse interdum diam egestas enim mollis viverra. Sed in porttitor odio. Nulla non dolor rutrum sem sodales sodales. Nam consectetur erat id tellus dapibus, in convallis nibh scelerisque. Aliquam interdum, arcu eget bibendum ullamcorper, odio magna euismod mauris, at laoreet felis lorem id justo. Vivamus pretium in nunc et laoreet. Integer magna leo, finibus id massa id, consectetur viverra erat. Fusce et pellentesque leo, ut dignissim nunc."
#     li = list(str.split(" "))
#     shuffle(li)
#     str1 = " "
#     a = str1.join(li).split()
#     for i in range(0, len(a), 10):
#         str1 += ' '.join(a[i:i + 10]) + '\n'
#     return str1

def getLorem(count):
    str =  """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eu vehicula velit. Phasellus pulvinar, diam volutpat commodo ultrices, dolor est efficitur metus, nec convallis magna urna ac arcu. Sed sodales lectus at fermentum convallis. Nullam mattis luctus odio, mollis bibendum enim accumsan vel. Aenean aliquet sapien ac maximus mattis. Praesent nec diam diam. Aliquam erat volutpat. Cras eleifend tristique lorem, at sagittis nibh dapibus eu. Morbi hendrerit mollis neque, ac feugiat mauris hendrerit non. Nunc vestibulum semper lobortis. Etiam hendrerit elit vel faucibus commodo. Nunc facilisis eget massa in porta. Nunc ac neque fermentum, lobortis orci vitae, faucibus ipsum.
            "Aliquam convallis, nunc non facilisis commodo, diam justo imperdiet justo, eget egestas purus enim eget arcu. Fusce dapibus ultricies massa sit amet ultrices. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aenean vitae risus et eros aliquet interdum. Aliquam in eleifend tortor. Proin mollis finibus tortor eget ornare. Maecenas rutrum blandit dignissim. Quisque laoreet ac est dapibus suscipit.
            Fusce pretium nisi nec tellus commodo egestas. Nulla porta magna mi, eget volutpat tortor venenatis id. Pellentesque congue malesuada finibus. Phasellus ac ante at ipsum efficitur ullamcorper vel pellentesque magna. Proin luctus ligula sed eros eleifend posuere. Ut vestibulum sollicitudin luctus. Sed nec nulla eget enim consectetur congue a sit amet eros. Integer semper convallis finibus. Nunc nunc odio, dictum non metus vel, congue lobortis dolor. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec id blandit massa, a accumsan urna.
            Sed cursus tellus sit amet tellus auctor, et mollis risus hendrerit. Pellentesque in urna in diam maximus convallis. Morbi scelerisque elementum efficitur. Mauris venenatis molestie dui, vel accumsan erat pellentesque non. Pellentesque volutpat hendrerit elit, nec venenatis lorem pharetra quis. Phasellus eu imperdiet felis. Sed fermentum mollis mi, at tempus enim. Cras convallis, ex vitae congue pretium, risus leo semper sapien, id facilisis lectus dui in purus. Ut elementum turpis sit amet facilisis rhoncus. Praesent accumsan quis felis eget scelerisque. Suspendisse eu fringilla nisi, vitae consectetur ex. Aliquam erat velit, volutpat a laoreet et, molestie et libero. Suspendisse 
            ut lacus at massa mattis elementum vel non ligula. Fusce felis enim, tristique in lorem vel, convallis blandit libero. Aliquam erat volutpat. Vestibulum sed libero enim.
            Sed tempus auctor ipsum, eleifend bibendum est tempor in. Cras nisl felis, placerat a accumsan elementum, feugiat scelerisque tellus. Vivamus et leo in velit ullamcorper tincidunt. Fusce molestie hendrerit viverra. Duis interdum malesuada posuere. Donec et pellentesque leo, sed pulvinar risus. Suspendisse congue dapibus lacus, ac tincidunt nunc pulvinar tempor. Proin venenatis sit amet nunc convallis blandit. Sed ac iaculis urna. Nam tincidunt libero quis consequat porttitor. Integer ut dictum nibh. Quisque consequat velit non sapien fermentum sollicitudin. Nunc nec enim sed neque eleifend vestibulum. Duis auctor ac orci id porttitor."""

    lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    li = list(str.split(" "))

    lit = []
    if count == 8:
        return lorem

    elif(count<=463):
        for i in range( 8 , count):
            lit.append(li[i])
            shuffle(lit)

    else:
        count = 463
        for i in range( 8 , count):
            lit.append(li[i])
            shuffle(lit)

    str1 = " "
    str1 = str1.join(lit)

    if (str1[-1] == ',' or str1[-1] == '.' or str1[-1] == '!' or str1[-1] == '?'):
        str1 = str1[:-1]
        str1 = ''.join((str1, '.'))
    else:
        str1 = ''.join((str1, '.'))

    return lorem +" "+ str1

    # feature for insert a new line for every 10 words
    '''
    str1 = str1.join(lit).split()
    a = str1.split()
    ret = ''
    for i in range(0, len(str1), 10):
        ret += ' '.join(a[i:i+10]) + '\n'
    return ret
    '''
