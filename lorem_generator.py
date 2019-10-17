from random import shuffle

def getLorem():
    str =  "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent non mi ut erat tincidunt placerat. Nam a enim semper, mattis mauris eget, mattis orci. Sed consequat nisi quis orci varius aliquam. Vestibulum a sem vitae nisl maximus porta. Duis blandit enim sed lorem placerat, eget sollicitudin lectus pellentesque. Etiam gravida non massa tristique ultrices. In hac habitasse platea dictumst. Suspendisse interdum diam egestas enim mollis viverra. Sed in porttitor odio. Nulla non dolor rutrum sem sodales sodales. Nam consectetur erat id tellus dapibus, in convallis nibh scelerisque. Aliquam interdum, arcu eget bibendum ullamcorper, odio magna euismod mauris, at laoreet felis lorem id justo. Vivamus pretium in nunc et laoreet. Integer magna leo, finibus id massa id, consectetur viverra erat. Fusce et pellentesque leo, ut dignissim nunc."
    li = list(str.split(" "))
    shuffle(li)
    str1 = " "
    return (str1.join(li))

# def getLorem():
#     return "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

# print(getLorem())