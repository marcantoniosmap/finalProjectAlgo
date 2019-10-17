from random import shuffle

def getLorem():
    str =  "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent non mi ut erat tincidunt placerat. Nam a enim semper, mattis mauris eget, mattis orci. Sed consequat nisi quis orci varius aliquam. Vestibulum a sem vitae nisl maximus porta. Duis blandit enim sed lorem placerat, eget sollicitudin lectus pellentesque. Etiam gravida non massa tristique ultrices. In hac habitasse platea dictumst. Suspendisse interdum diam egestas enim mollis viverra. Sed in porttitor odio. Nulla non dolor rutrum sem sodales sodales. Nam consectetur erat id tellus dapibus, in convallis nibh scelerisque. Aliquam interdum, arcu eget bibendum ullamcorper, odio magna euismod mauris, at laoreet felis lorem id justo. Vivamus pretium in nunc et laoreet. Integer magna leo, finibus id massa id, consectetur viverra erat. Fusce et pellentesque leo, ut dignissim nunc."
    li = list(str.split(" "))
    shuffle(li)
    str1 = " "
    a = str1.join(li).split()
    for i in range(0, len(a), 10):
        str1 += ' '.join(a[i:i + 10]) + '\n'
    return str1
