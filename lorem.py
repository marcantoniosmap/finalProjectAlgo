loremString='''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eu sem maximus, volutpat purus sit amet, semper enim. Quisque consequat ac neque a fermentum. Donec id semper orci, a vehicula augue. Pellentesque condimentum risus ac est pulvinar gravida. Morbi id diam tincidunt, pulvinar sem ut, porta tellus. Phasellus est elit, feugiat vel sagittis sit amet, faucibus gravida nisi. Aenean quis tristique libero. Vivamus venenatis turpis eu sapien ornare dignissim. Morbi ornare viverra commodo. In mattis risus orci, venenatis porttitor erat dignissim at. Aenean malesuada non ex ac commodo. Maecenas hendrerit urna vitae nisl placerat blandit. Quisque fermentum euismod est ut gravida. Quisque sit amet congue sapien. Maecenas rhoncus massa neque, nec placerat quam fringilla ut. 
Integer euismod, turpis a ultrices tincidunt, tellus ipsum aliquam justo, et tincidunt neque quam sit amet turpis. Sed convallis varius dolor suscipit bibendum. In dapibus viverra ultrices. Etiam faucibus vehicula auctor. Sed consectetur nulla ac aliquam euismod. Donec sit amet mollis tortor, vitae sodales est. Nullam rhoncus urna ac ex aliquet maximus. Vivamus commodo a augue vitae iaculis. Praesent sed ipsum porttitor, elementum neque ac, viverra nibh. Sed eleifend eros dui, sit amet iaculis mi auctor et. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nam rhoncus erat sit amet hendrerit ultricies. 
Curabitur imperdiet odio sit amet consectetur semper. Integer imperdiet maximus rutrum. Vivamus posuere purus lorem, nec scelerisque dolor consequat sit amet. In eu vehicula augue. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Ut molestie egestas arcu, eget efficitur ex finibus ut. Nulla facilisi. 
Nunc dapibus nunc nec sem ornare, ac dignissim nisi rutrum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris egestas, ante non finibus venenatis, nisi arcu tincidunt ex, id pellentesque turpis nulla quis nunc. Donec neque mi, semper ut ex lacinia, efficitur ornare est. Etiam dui massa, sodales in pulvinar sit amet, malesuada vel odio. Nulla vitae lacus semper, condimentum augue eget, tempor nisi. Praesent ex magna, congue sit amet nibh eget, condimentum pulvinar dolor. Mauris id tempor sapien. Proin vulputate consectetur felis, a bibendum turpis pretium et. Nulla maximus blandit tellus, vel tristique nunc. Donec placerat bibendum metus, malesuada placerat dolor eleifend ut. Curabitur leo libero, porta sit amet eleifend vel, condimentum at neque. Suspendisse quis rhoncus enim. '''

loremList=loremString.split(' ')

def formatted(s):
    if s[-1]==',':
        s=s[:-1]
        s=s+'.'
    elif s[-1].isalnum():
        s=s+'.'
    return s

def getLorem(word):
    if word > len(loremList):
        s=''
        count=len(loremList)
        total=0
        while count > 0:
            s=s+' '.join(loremList[:count])
            total=total+count
            count=word-total
        return formatted(s)

    else:
        return formatted(' '.join(loremList[:word]))


def getLoremParagraph(tag):
    if tag=='p':
        return getLorem(40)
    else:
        return getLorem(10)

