

#SYNTAX:
tags:   {

    div,
    span,
    p,
    h1,
    h2,
    
}

SIBLING TAGS: '+'
creates a sibling tag after last Tag
example:
    >> div + span
{
    <div>
     </div>
     <span>
     </span>
     
}

CHILDREN TAGS: '>'
creates a tag inside the last tag
example:
    >> div > span
{
    <div>
     <span>
     </span>
     </div>
     
}

MULTIPLY TAGS: '*'
creates a copy of an last tag
example:
    >> div * 3
{
    <div>
     </div>
     <div>
     </div>
     <div>
     </div>
     
}

ID TAGS: '#'
setting the ID on the last tags
example:
    >> div #marc
{
    <div id='marc'>
     </div>
}

CLASS TAGS: '.'
setting the class on the last tags
example:
    >> div .marc .amar
{
    <div class='marc amar'>
     </div>
}

CLIMB UP TAGS: '^'
going one up the parent's tag
example:
    >> div >p ^ span
{
    <div>
    <p>
    </p>
     </div>
     <span>
     </span>
}


CONTENT TAGS: '{_}'
setting the content on the current tags
example:
    >> div {hai there}
{
    <div>
        hai there
     </div>
}

LOREM AUTOMATION: '{lorem}' or '{lorem*10}'
setting the content on the current tags as a dummy text,
can be specified by words count or automatize based on tag
example:
    >> div {lorem}
{
    <div>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eu.
     </div>
}

    >> div {lorem*2}
{
    <div>
        Lorem ipsum.
     </div>
}


