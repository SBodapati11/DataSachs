import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Help Me Learn Finance!",
    page_icon="👀",
)

st.write("# Help Me Learn Finance!")
st.write("## ft. a pair of headphones 🎧")
st.write("### TL;DR - Risk Analysis is important, and we need to know what it means!")

st.markdown(
    """
    Even though America says that it runs on Dunkin, the truth is that America really runs on money. And if you don't know what to do with that money early on, you can find yourself up a creek without a paddle. And usually, what people do in order to ensure their long-term financial success, is build up something called a **portfolio**. What exactly is a portfolio? Well, think of it as a showcase, where different properties and assets show off their value for you to use later on. In its most basic terms it is essentially an important tool for ensuring your long-term Financial success, for you are able to see patterns in it and make decisions based on set patterns. 

    That being said, it's also not something that many people take into account, primarily because at first glance it seems so complex. And honestly it definitely sounds that way at first glance. After all there's so many different **financial vehicles** that are available to you, that it's very difficult to pick which one to drive. I mean, you get all these different types of options: like traditional IRA, Roth IRA, Social Security, et cetera; and it's very easy to get caught up in all of this. And while Vehicles like IRAs are one of those things that your parents may tell you to invest in and you let it sit and let it slowly grow over time, the important truth is to understand that no matter how simple these investments seem to be, they will always have one factor associated with them - risk.
    
    **Risk** is always there in every single decision we take. To set this up, let’s use an example. Suppose I'm a big headphone buff. I don't need to suppose; I know I am! So let's say I saved up for them, and the payoff has been immense. But let’s say that I didn’t buy it at market price. Let’s say that I chose a third-party seller who is selling them at 25% off the original price. Sounds like a great deal on paper, right? But there’s not as many guarantees. What if it doesn’t have a warranty? What if the headphones are some knockoff? That is a risk that I’m willing to take.
    
    A common misconception is that risk is negative, but that’s not always true. Risk is how much you’re willing to give up to get what you want. In the case of the headphones, I was willing to give up credibility and a money-back guarantee for a seemingly lower price. **Risk analysis** is often avoided because it's very easy to have your eyes on the money but not have your eyes on everything else around you. If there's anything that this market and inflation has shown us, it's that our future, especially our financial future, can always swing either way. Is that something that we can easily mitigate by ourselves? Maybe one day. But the more practical solution would be to learn how to manage your wealth while minimizing the risk in investing it.
    
    **DataStacks** was created with that in mind, giving short-term knowledge for long-term gain and growth. We seek to fulfill that mission by helping people like me who have absolutely no financial knowledge whatsoever, understand the importance of risk analysis, and in order to do so, we use models that attempt to track these types of changes in order to discern patterns. Granted, in doing so we can't always guarantee what is going to be the best outcome because the financial market is that unpredictable. But we also know that risk involved can be minimized, and for beginners, we recommend investments based on that. That is the question that we seek to answer. The question is, however, are you willing to take the chance?

    """
)

image = Image.open('images/DataStacksIcon.png')

st.image(image, caption='DataStacks')

