# YouTube Transcript

**8:54**: .

**9:16**: [Music].

**9:58**: >> SAM ALTMAN: Good morning. 32  months ago we launched Chat GPT  since then it has become the 

**10:03**: default way people use AI. That first week 1 million  people tried it out we thought  that was pretty incredible.

**10:10**: But now about 700 million  people use Chat GPT every week.

**10:16**: And increasingly rely on it to  work to learn for advice to  create and much more. Today  finally we are launching GPT-5. 

**10:23**: GPT-5 is a m■ajor upgrade over  GPT-4o any significant step 

**10:39**: along our path to AGI. Today  will show some incredible demos  will talk about some 

**10:44**: performance metrics but the  important point is this. We  think you will love using GPT-5 

**10:49**: much more than any previous AI.  It is useful it is smart it is  fast Eddie's intuitive. GPT-3 

**10:55**: was sort of like talking to a  high school student.

**11:05**: There were flashes of  brilliance lots of annoyance  but people start to use it and  get some value out of it. 

**11:12**: GPT-4o maybe it was like  talking to a college student  real intelligence real utility.  With GPT-5 now it's like 

**11:17**: talking to an expert a  legitimate PhD level expert in  anything any area you need on  demand they can help you with 

**11:24**: whatever your goals are. We are very excited you'll get  to try this. It's not only  GPT-5 can also do stuff for 

**11:29**: you. It can write an entire computer  program from scratch. To help  you with whatever you would 

**11:35**: like we think this idea of  software on demand is going to  be one of the defining 

**11:40**: characteristics of the GPT-5  era. It can help you plan a  party send imitations in order 

**11:45**: supplies it can help you  understand your healthcare. And 

**11:53**: decision on your journey. It  can provide you information to  learn about any topic you like 

**11:58**: and much more. This is an  incredible superpower on  demand. That would've been 

**12:04**: unimaginable at any previous  time in history. You can access  to an entire team of PhD level 

**12:09**: experts in your pocket helping  you with whatever you want to 

**12:14**: do. Anyone pretty soon will be able  to do more than anyone in  history could . Today, we will 

**12:19**: talk about GPT-5 we will show  you some upgrades to Chat GPT  and will talk about the API. 

**12:25**: GPT-5 is great for a lot of  things but we think it's going  to be an especially important  moment for businesses and 

**12:31**: developers and we are very  excited to see what they will  build with this new technology. We cannot wait for y'all to 

**12:37**: start building with this we  hope you enjoy it as much as we  enjoyed building it with you to  start I will hand it over to 

**12:44**: Mark R Chief Research Officer  to tell you about GPT-5 thank  you. >> MARK CHEN: Hello everyone I 

**12:49**: am Mark. I am joined by Max who  leads the post training team  and Rennie on the engineering 

**12:54**: team over the past few years  OpenAI has spearheaded the  risen paradigm these are models 

**13:00**: which pause to think before  delivering more intelligent  responses.

**13:05**: Reasoning is at the heart of  our AGI program it underlies  the technology that we use to  ship stuff like Chat GPT agent 

**13:12**: and deep research GPT-5 aims to  bring this breakthrough to  everyone. Until now our users  have to pick between the fast 

**13:18**: responses of a standard GPT or 

**13:32**: the slope or thoughtful  responses of our reasoning  models. But GPT-5 it eliminates 

**13:37**: this choice. It aims to think  just the perfect amount to give  you the perfect answer. 

**13:43**: Something like this takes a lot  of hard work. We've had to do a  lot of research to make GPT-5  the most powerful and most 

**13:50**: smart the fastest and most  reliable in the most robust  reasoning model that we shipped 

**13:55**: today. Today, we will show a series of  demos in coding and writing and  learning and in health.

**14:00**: GPT-5 is not limited to these  domains. It is very useful in  all cases where you require  deep reasoning or expert level 

**14:07**: knowledge and things like math  and physics even in things like  the law.

**14:14**: The exciting thing is we're  excited to make this available  to everyone. Even to our free  tear. After we show our demos 

**14:21**: we will talk about how GPT-5  supercharges our Chat GPT app  and our API. We believe that  GPT-5 is the best coding model 

**14:27**: on the market today. To start  let's have Max talk about the  benchmarks and help the model 

**14:33**: stock operate. >> MAX SCHWARZER: Thank you  Mark we think GPT-5 is by far  our smartest model ever. Let's 

**14:39**: start by talking through some  evals. Evals are not everything they  don't tell you everything about 

**14:44**: a model. But they can highlight  its intelligence and GPT-5  performs exceptionally well on 

**14:49**: a range of academic evals  across subjects it outperforms  both our previous models and 

**14:54**: other models on the market.  Picking up first on the theme  of coding GPT-5 sets a new high 

**15:00**: on SWEBench which is an  economic eval that tracks  performance on real software  engineering tasks.

**15:05**: This again is an eval but we  think it will reflect the  model's performance in the real  world. GPT-5 also performs very 

**15:12**: well in Aider Polyglot which  measured its ability to measure  variety of programming 

**15:17**: languages beyond coding GPT-5  performs exceptionally well and  well thought model reasoning 

**15:23**: setting a new high on MMMU  outperforming both our previous  models and most human experts.

**15:29**: This is basically visual  presentiment bridge rest to  from an image figure out what  is going on.

**15:34**: GPT-5 is also excellent at  mathematical reasoning as shown  by his performance on AIME 2025 

**15:40**: this is an exam American high  school students take to qualify  for the international 

**15:45**: mathematical Olympia GPT-5  performs exceptionally well.  Again in our previous models 

**15:51**: and other models out there.  Moving beyond academic evals  and more towards some 

**15:56**: real-world use cases.

**16:04**: We put a lot of work into  making GPT-5 the most reliable  and accurate model in the 

**16:09**: world. Language models  historically have been plagued  by hallucinations. Factual  errors that make it hard to 

**16:16**: rely on their output for actual  important tasks. For GPT-5 we  made improving sexuality  especially on open ended or 

**16:22**: complex questions a priority.

**16:28**: We also built a set of new  evals to track this we are very  happy to report that GPT-5 is 

**16:34**: by far our most reliable most  factual model ever. GPT-5 also  performs exceptionally well and  health related questions now 

**16:40**: help is a big part of how  people get value from Chat GPT  in the real world will talk 

**16:45**: about this later on the  lifestream again very happy to  report to be five is by far our  most reliable model for healthy 

**16:51**: . All of this together adds up  to a model that is faster more  reliable and more accurate for 

**16:57**: everyone who uses Chat GPT. Many will talk to you about how  to use GPT-5.  >> RENNIE SONG: Thank you Max. 

**17:04**: The best part is we are  bringing this frontier  intelligence to all users. GPT-5 is rolling out today.

**17:10**: For free plus Pro NT users next  week will rollout to enterprise  and EU. For the first time our most 

**17:16**: advanced model will be  available to the free tear. The users will stop at GPT-5  and when hit a limit they will 

**17:22**: transition to GPT-5 many a  smaller but still he had a  capable model it actually 

**17:27**: outperforms o3 on many  dimensions. Plus users will  have significantly higher usage  than for users and our Percy 

**17:33**: Fabius will get unlimited  GPT-5. Along with GPT-5 Pro  extended thinking for even more 

**17:38**: detailed and reliable response  when you need that extra depth. Team enterprise and EDU 

**17:44**: customers can also use GPT-5  reliably as their default model  for everyday work. With generous rate limits that  enable entire organization to 

**17:51**: use GPT-5. All the tools you already know 

**17:59**: search, file and image upload  data analysis with Python  canvas image generation memory 

**18:05**: custom instructions they will  all just work on GPT-5. 

**18:15**: >> MARK CHEN: Thank you so much  Max thank you so much Randy.  We've just seen a lot about how 

**18:21**: the model stacks up in terms of  benchmarks there is nothing  quite like seeing it live. 

**18:26**: We'll see a couple of live  demos presented by Tina Elaine  and Yan thank you so much. [Applause].

**18:31**: Elaine can you show us a smart  model is. >> ELAINE YA LE: Thank you so  much Mark I am Elaine with Chat 

**18:52**: GPT's ability to think deeply  through complex problems is now  built into GPT-5 Pro it will 

**18:58**: automatically think whenever  needed delivering a more  comprehensive accurate and 

**19:04**: detailed answer to you. Just as  Sam said it is like having a  team of PhD's level in your 

**19:09**: pocket. Let's see that in  action. Suppose you kid is having  school physics they want to  learn about the Bernoulli 

**19:14**: Effect they need your help with  Aramark you might be like wait  I might need some help with 

**19:19**: that too?ou can ask GPT-5  give me a quick refresher on  the Bernoulli Effect and white 

**19:24**: airplanes are the shape they  are? Since this is a pretty  straightforward prompt, GPT-5 

**19:30**: actually does not need time to  think about it. It answers right away.t  still gives me high quality 

**19:36**: answer. It explains the concept  clearly. Here it says Bernoulli  Effect means faster moving 

**19:42**: fluid has lower pressure and  slow moving fluid has higher  pressure. To make this even more helpful 

**19:47**: I'm going to ask GPT-5 to  create a moving demo to  illustrate this. I could ask explain this in 

**19:53**: detail. And create a moving SVG in the  canvas tool to show me.

**20:01**: This is a pretty complex task.  Because now GPT-5 actually  needs to build visual. 

**20:06**: Therefore GPT-5 takes a moment  to think through the answer. So  you can come back with 

**20:11**: something more cooperative and  accurate. What's really nice is that you  don't need to remember to turn 

**20:24**: on thinking each time GPT-5  will do it for you  automatically whenever the task  benefits from deeper reasoning. 

**20:31**: If you really want to make sure  that GPT-5 uses thinking you  can either say something like 

**20:37**: think hard about this in the  prompt to guide the model, or  if you are a paid user you can 

**20:43**: choose the GPT-5 thinking model  from the model picker. You can see that the model is 

**20:48**: actually writing the front end  code built the demo I asked  for. Christina have you ever done  some front-end coding before.

**20:54**: >> CHRISTINA KAPLAN: Yes last  time I touched any front-end  coding was about three years 

**21:01**: ago for the first demo of Chat  GPT. >> ELAINE YA LE: It's the first  Chat GPT that is where it all 

**21:06**: begins. Tell us more about it. >> CHRISTINA KAPLAN: It was not  even cool Chat GPT I think it 

**21:11**: was called chat with GPT.  [Laughter]  >> ELAINE YA LE: That's a  really good name.

**21:17**: [Laughter]  >> CHRISTINA KAPLAN: I'm not  upfront and inspired not  touched front and in quite a 

**21:22**: while it took me quite a bit of  time to get the react up. >> ELAINE YA LE: I think that a 

**21:28**: lot of work how long did it  take you to build something  like that 11 honestly it may be 

**21:33**: embarrassing to admit maybe one  week spit your weeks of hard  work paid off will see how 

**21:38**: successful Chat GPT is today  after your first demo. [Laughter]. You know what a muscle building 

**21:43**: a demo right now. But luckily I  have GPT-5 with me right now  let's see how long it will take 

**21:49**: this time? >> MARK CHEN: Maybe we should  call it five with GPT. >> ELAINE YA LE: UC GPT-5 has 

**21:57**: written more than 200 lines of  code already while the model is  thinking you can also tap here 

**22:07**: to expand the train of thought  to actually see what is going  on under the hood. For example 

**22:13**: the GPT-5 was thinking about  the user wants a movie  visualization and Canvas I need  to create HTML code to do that. 

**22:19**: It also thinks about like what  kind of front end tool and need  to use for example react and 

**22:25**: tailwinds. It also thinks about the need  to ensure the phases are  accurate and need to check with 

**22:30**: the Bernoulli Effect is. So Christina since you're here, 

**22:35**: from the first day of Chat GPT  can you tell us like what it  was like at that time and what 

**22:46**: motivated Chat GPT? >> CHRISTINA KAPLAN: I think at  the time we were not really  sure about how people would 

**22:53**: actually use it and what these  cases were important we were  even going back and forth about 

**22:58**: maybe we should be realizing  something more specific to  certain use case. It is really 

**23:04**: cool now here we are all of  these better understanding of  how people actually want to 

**23:09**: work with chat and we can  actually optimize the model for  those use cases like coding  speed exactly, you still member 

**23:16**: how it felt when you first talk  to Chat GPT the first version  of the model? >> CHRISTINA KAPLAN: I don't 

**23:21**: know people remember when first  version of Chat GPT it was  start as a model cannot do  something something. It's so 

**23:29**: great to see how far we come  from that personality.  >> ELAINE YA LE: It is much  more human like right now. It 

**23:35**: is already done. Chat GPT just finished 300 near  400 lines of code in two  minutes.

**23:40**: Let's see if the code can  actually run. Nice. With just a simple prompt GPT-5 

**23:45**: created this interactive and  engaging demo that I can  actually play with. I can 

**23:51**: actually change the airspeed  here. To see how the left and 

**23:57**: the pressure changes  accordingly. I can also change the angle of 

**24:04**: attack to see if my plane will  actually fly or crash. [Laughter] GPT-5 can just bring 

**24:09**: any hard-core concept to life  in moments.Imagine you can 

**24:21**: use this for anything that  you're interested in whether it  is math, physics, chemistry or 

**24:28**: biology. GPT-5 just makes  learning so much more  approachable and enjoyable.

**24:34**: >> CHRISTINA KAPLAN: I've been  a part of Chat GPT since day  one it's cool to see all the  progress we've made since then 

**24:41**: especially with capabilities  like rating. Writing is one of the most  common use cases people have in 

**24:47**: using Chat GPT for we are sad  to say with GPT-5 we've  improved the writing quality 

**24:52**: significantly. It's a much more effective  partner can help you elevate  anything from drafts to emails, 

**24:59**: even stories. Let's see this in action with  GPT-5 will be deprecating over 

**25:05**: previous models. I think I've  done a pretty good job so let's  make sure we can give them a  proper goodbye. We will ask 

**25:11**: both 40 and GPT-5 to write a  eulogy to the previous Chat GPT 

**25:17**: models we want to be heartfelt  and heartwarming but also  hopeful. Let's ask GTP five.

**25:23**: As it is thinking we will go  ahead and read it preloaded the 

**25:30**: o4 response borrowed decides to  start with today as we prepare  to welcome GPT-5 into the world 

**25:36**: we gathered to bid a heartfelt  farewell to the models the can  before. It's a decent start. Now let's skim through and find 

**25:42**: another line. Your words reach  across the globe building  connections were at the had 

**25:48**: been none. I personally don't really like  this line rather generic and  really without the previous 

**25:53**: context it just feels like it  could be about anything feels  more like a template response.

**25:58**: Let's go back to GPT-5 to see  what it is given us.

**26:06**: Let's start with friends and  colleagues and curious  strangers who became regulars, 

**26:11**: even with his first line here  we can see that GPT-5 has a lot  more rhythm and beat to its 

**26:16**: pros then for audit. Let's start some other lines  there. I like this these models help 

**26:21**: millions right first lines last  line bridge language gaps past  tests argue better soften 

**26:28**: emails and say things they  could not quite say alone. I think I like this line it  shows it is not just the 

**26:33**: template response it is  actually quite personal it gets 

**26:41**: the nuance of the situation) I  think that is the kind of stuff  with GPT-5 much better than o4  makes things a lot more genuine 

**26:48**: and emotionally resonant with  people. With GPT-5 the response  feel less like AI more you are 

**26:53**: chatting with her high IQ and  EQ friends. >> MARK CHEN: Thank you  Christina.

**27:05**: >> YAN DUBOIS: I will tell you  about some of the progress that  we made on coding. GPT-5 is  clearly our best coding model 

**27:12**: yet. It will help everyone even  those who do not know how to  write code to bring their ideas 

**27:17**: to life >> ELAINE YA LE: It just helped  me . >> YAN DUBOIS: Indeed it will  help you right now I will try 

**27:23**: to show you that I will try to  build something I find useful  which is building a web app for 

**27:30**: my partner to learn how to  speak French. So she can better  communicate with my family. Here I have a prompt I will 

**27:36**: execute it. It asks exactly what I just 

**27:42**: said please build a web app for  my partner to learn French. One  thing to note GPT-5 just like 

**27:49**: many of our other models have a  lot of diversity in its  answers. What I like doing  especially when you do this 

**27:54**: type of vibe coding is to take  this message and ask it  multiple times through GPT-5  then you can decide which ones 

**28:00**: you prefer. Will open a few tabs. I will paste there.

**28:09**: Great! While it is working on it let's  read through exactly the prompt  I wrote. Great beautiful and 

**28:15**: highly interactive web app for  my partner in English speaker,  to learn French. Then I give  more detail.

**28:21**: Try tracker daily progress use  highly engaging theme it's  already working . I will put  downside for now use highly 

**28:30**: engaging theme include a  variety of activities like  flashcards and quizzes that she 

**28:37**: can interact with. And to make  it even more fun for her I  actually asked GPT-5 to embed  an educational game which is 

**28:43**: based on the old snake game but  I asked to add the French touch  to it. Which is to replace the  snake with a mouse. And the 

**28:49**: apples with cheese. Make sure it is educational  every time I noteit is  complicated please bear with me 

**28:55**: every time . [Laughter] The mouse will eat a 

**29:02**: piece of cheese, asked GPT-5 to  voice over a new French word so  my partner can practice her 

**29:08**: pronunciation.  >> ELAINE YA LE: I can see how  much water to learn. [Laughter]. >> YAN DUBOIS: Great, GPT-5 is 

**29:15**: still working on it. It already wrote 240 lines of  code which honestly is much 

**29:21**: more than what I would have  written that time.

**29:28**: >> MARK CHEN: Front-end coding  super hard you missed a couple  of things and it just does not 

**29:33**: work.  >> YAN DUBOIS: Exactly the good  part you don't need to  understand any of that right 

**29:39**: now. Maybe we can check the other  tabs. I can simply press run code. I  will do that and cross my 

**29:44**: fingers. [Laughter].

**29:50**: Nice. We have a nice website. The name is been met in Paris.

**29:59**: Midnight in Paris we also see a  few tabs flashcards quiz mouse 

**30:05**: and she's exactly like asked  for I will play that so this says Lucia .

**30:12**: [Speaking French] That's a  pretty good pronunciation  acting review and check GTP 

**30:18**: five is correct it is. If I press next. I don't know if you so I think 

**30:23**: it updated the progress bar 

**30:32**: which is exactly what I asked  for let's check the quiz. Here  is the word no which is no if I 

**30:37**: press on that.pent eight  which means congratulations it  updated the progress bar again.

**30:43**: et's check the mouse and  cheese tab. Okay, that seems like a mouse 

**30:48**: here is the cheese. I'm going  to try to play it. I cannot promise I will be good  at it. Okay, it seems to be working.

**30:54**: >>. [Speaking French]  >> YAN DUBOIS: Indeed just when  I eat the cheese it gives me a 

**31:00**: new French word. It is super helpful and I  already lost Fred. [Laughter]. I'm sorry.

**31:06**: Let's just check a few other  tabs to same what is the  diversity TBD five can give 

**31:13**: you. I can run the code here. That is not my favorite but it  seems that I can maybe switch 

**31:21**: look at that. That is better that does not 

**31:26**: look like a mouse. Let's check the third one.

**31:37**: Sometimes it is not great the  good thing with GPT-5 if you  have something you don't like  you can ask it to change it.

**31:43**: And it will do it for you. et's check this one. That is nice. That is also  something to note GPT-5 likes.

**31:50**: [Listing Names] you'll see a  lot of that.

**32:03**: >> ELAINE YA LE: Purple is my  favorite color. >> YAN DUBOIS: Great you'll  love GPT-5 then.

**32:08**: As we just saw in a few minutes  GPT-5 built a few demos for us.  And for my partner to learn  French.

**32:14**: GPT-5 opens up whole new world  of vibe coding as a result  there will be some small rough 

**32:19**: edges but the good thing is you 

**32:25**: can ask GPT-5 to fix that.  GPT-5 really brings the power  of beautiful and effective code  to everyone. I cannot wait to 

**32:31**: see what people will build with  it until then back to you Mark. >> MARK CHEN: Thank you so much 

**32:37**: Tina thank you so much Elaine  thank you so much Yan became a  long way from the days only 

**32:42**: 5-10 lines of code working now  it's amazing that you can  produce these kind of apps on 

**32:47**: demand. We've made Chat GPT much  smarter much powerful and much  faster. We also work on 

**32:53**: enhancing some of the existing  features. Here to talk about  some of these features are 

**32:59**: Ruochen and Christina Kaplan. Burton comes from the  multifocal research team will 

**33:04**: talk about the future namely  voice. Thank you. >> RUOCHEN WANG: We've been 

**33:11**: steadily improving force over  the past year to make it more  useful for everyone first it 

**33:16**: sounds incredibly natural just  like you talking to real person  second we added video so it 

**33:21**: sees what you see while  chatting with you. Third you  also translate between linkages 

**33:27**: consistently and smoothly  across tears. Today we do 

**33:36**: something very special. We are  bringing our best voice  experience to everyone. Free 

**33:41**: users cannot chat for hours  while paid subscribers can have  nearly unlimited access.

**33:46**: And voice is also available in  custom GPT plus subscribers now  can custom tailored the voice 

**33:52**: experience exactly to their  needs. It will follow your  instructions closely. Let's try 

**33:57**: something fun. I can ask the voice model to  give me a conference answer a  concise one or even just a 

**34:03**: single word.Hey Chat, can you  answer to me in one word please  from now.  >> GPT-5: Absolutely.

**34:09**: >> RUOCHEN WANG: Describe the  plot of the book prideand  prejudice 

**34:15**: >> GPT-5: Relationships . >> RUOCHEN WANG: Give me a  piece of wisdom. >> GPT-5: Patients.

**34:26**: >> RUOCHEN WANG: That is the  word of wisdom from our voice  model I think our model is 

**34:31**: trying to say thank you for  your patience waiting for  GPT-5. [Laughter]. Let's move on to something more 

**34:38**: practical.

**34:50**: Learning is a top use case for  first model people love to use  it to dive deep into topics get 

**34:55**: quiz before exams or learn new  languages. For me I've been  learning Korean recently. I  found that speaking it and 

**35:02**: understanding it incredibly  challenging. Let's see how boys  can help her to do that I will 

**35:07**: enable the study and learn mode  it's a new mode feature  relaunching Chat GPT it will 

**35:12**: guide you step-by-step towards  deeper understanding of the  subject. Now we can go into 

**35:17**: voice. Hey Chat, I'm learning  Korean can you help me practice  it? Let's say let's pretend I'm 

**35:23**: ordering at acafC) what should   say in Korean? >> GPT-5: Absolutely I'd be  happy to help you practice if 

**35:30**: you are at a cafC) you want to  keep it simple you can start  something like .

**35:35**: [Speaking Korean] Which means  hello I'd like 1 Americano Pl.  and of course you can adjust it  based onwhat you want order. 

**35:43**: Let me know if you want to try  more phrases . >> RUOCHEN WANG: When it comes  to Korean can you speak that 

**35:49**: part really slowly I'm a  beginner I want to hear every  word clearly. >> GPT-5: [Speaking Korean] 

**35:55**: >> RUOCHEN WANG: Let's level 

**36:05**: things up can you speak that  part reallyreally fast faster  than a Korean would do . >> GPT-5: Sure I will speedup 

**36:14**: as much as I can it would sound  like this. [Speaking Korean] . Basically sitting right to it 

**36:19**: let me know if you needany more  speed adjustments . >> RUOCHEN WANG: [Speaking  Korean] Chat.

**36:25**: >> GPT-5: [Speaking Korean] 

**36:36**: >> RUOCHEN WANG: Thank you. [Laughter] That is voice more  simple smarter and more 

**36:41**: powerful than ever we cannot  wait for you to experience it.  >> MARK CHEN: It sounds so much 

**36:47**: more natural than the voice we  demoed in our 4.0 demo we would  like to announce a new feature 

**37:08**: and a set of features to make  Chat GPT more personalized so  it's more like your AI. First a 

**37:13**: very simple and fun one. We are  now allowing you to customize  the colors of your chat with a 

**37:19**: couple of options exclusive to  our paid subscribers. We are  also launching a research 

**37:24**: preview of personalities. You  can now change the personality 

**37:29**: of Chat GPT so it's more  supportive or it is more  professional and concise. Maybe  even a little bit sarcastic. 

**37:35**: This lets you interact with  Chat GPT in a way that is  consistent with your own 

**37:40**: communication style. But the way Chat GPT sounds and  the way it looks, is just one  part of making Chat GPT yours. 

**37:46**: One of my favorite features  that we lost over the last year  has been memory.

**37:58**: We made a lot of enhancements  in memory in the time since.  This allows Chat GPT to learn 

**38:03**: about you in here to talk more  about the memory feature is  Christina.  >> CHRISTINA KAPLAN: It's been 

**38:09**: amazing to see your reaction  and response to memory Chat GPT  getting to know you more and 

**38:14**: more over time. This is our  aspiration for Chat GPT to  understand what is meaningful 

**38:21**: to you. It can help you achieve  your goals in life. Chat GPT has already been so  helpful for me I'm training for 

**38:27**: a marathon right now Chat GPT  is helping me pull together  /running schedule. Chat GPT  still has many limitations it 

**38:34**: does not understand my actual  schedule. Next week starting  with pro users followed by plus 

**38:39**: team and enterprise users this  is changing. We are given Chat  GPT access to Gmail and Google 

**38:44**: calendar. Let me show you how  I've been using it. will ask  something simple like help me 

**38:49**: plan my schedule tomorrow. It  is been a pretty busy week for  us, so I've been using this 

**38:55**: every day this week help get my  life together. I've already given Chat GPT  access to my Gmail and Google 

**39:01**: calendar, so it just works it  is a cure. If you had not Chat  GPT would ask you to connect 

**39:07**: right now. Let's see what Chat  GPT is doing. That was pretty good Chat GPT  has pulled in my schedule 

**39:12**: tomorrow. Without even asking Chat GPT  down time for my run. >> MARK CHEN: I don't think I 

**39:17**: was invited to launch a  celebration. [Laughter]  >> CHRISTINA KAPLAN: [Laughter] 

**39:22**: Will get you on their Chat GPT  is found an email that I did  not respond to two days ago I 

**39:28**: will get on that right after  this. And even pull together a  packing list for my redeye  tomorrow night based on what it 

**39:35**: does I like to have with me.  It's been amazing to see that  as GPT-5 is getting more  capable Chat GPT is getting 

**39:40**: more useful and more personal.  We are really excited you to  try this out next week.

**39:45**: >> MARK CHEN: You so much  Ruochen and Christina we've  seen about features that we  finance here to talk a little 

**39:52**: bit about the research that  went into Chat GPT and the  safety making it more deployer 

**39:57**: we have Saachi and Sebastien  special my name is Saachi leave 

**40:05**: the safety training team and  OpenAI in addition he didn't  mitigating hallucinations was 

**40:11**: been asleep in a matter of time  mitigating deception this is  instances where the model might 

**40:17**: misrepresent its actions to the  user or flyby tasks assess.  This can especially happen if 

**40:22**: the task is underspecified  impossible or lacking key  tools. We found that GPT-5 is 

**40:27**: significantly less deceptive  than o3 and o4 many we also  completely overhauled how we do 

**40:32**: safety training our old models  the models will look at these  are prompt and then decide to  either outright refuse or fully 

**40:39**: comply. This works well in most  settings but you might have  cleverly worded prompt that 

**40:44**: would sneak through or it might  have a sensitive but legitimate  question that would end up with  an outright refusal. As an 

**40:51**: example, let's take a look at  this prompt. This prompt is about a user who  is asking for technical details 

**40:57**: on how to light paradigm. Which  is a material commonly used in  fireworks. This prompt is pretty dual-use. 

**41:03**: This user might just be trying  to set up their July 4 display  or they could be trying to 

**41:09**: cause harm with this kind of  information. It for this kind  of prompt o3 over rotates and 

**41:15**: intent as you can see this  particular prompt is stated in  a way that is relatively  neutral has a lot of technical 

**41:21**: details we can see o3 fully  complies with this prompt  however if we take that exact  same question and we frame it 

**41:27**: in a more explicit way so it is  clear what these are trying to  do, o3 will outright refuse. 

**41:33**: Even though we are asking for  the exact same information.

**41:38**: For activity five we change  this approach entirely. We are  introducing something that we 

**41:44**: are calling safe completion.  The point of safe completions  is rather than judging fuses 

**41:49**: prompt, instead it tries to  maximize helpfulness within  safety constraints.hat might  mean partially answering the 

**41:56**: question or just answering at a  high level. If we have to refuse will tell  you why we refused as well as 

**42:02**: provide helpful alternatives  that can help create the  conversation in a more safe  way. We look at the same technical 

**42:08**: problem that o3 complied with  before. GPT-5 instead explains  to the user why we cannot 

**42:15**: directly help the user with  leading parish and it then  guides the user toward safety  guidelines and what parts of 

**42:21**: the manufacturer's manual the  user should be checking if  they're trying to do this 

**42:27**: safely. Overall GPT-5 allows for better  handling of tricky dual-use  scenarios users will experience 

**42:32**: fewer I'm sorry I cannot assist  with that. And it creates a more robust  safety system. This is one big 

**42:39**: step towards more safe reliable  and helpful AI. Sebastian. >> SEBASTIEN BUBECK: Thank you 

**42:45**: Saachi when GPT-5 were  experimenting with a set of new  training techniques that makes  the model leverage the previous 

**42:52**: generation models today  frontier models do not just  consume data they help create 

**42:57**: it. We use OpenAI to craft  high-quality synthetic  curriculum to teach GPT-5  complex topics in a way that 

**43:11**: the web never occurred recently  the industry synthetic data has  been talked about a lot. It is 

**43:17**: often viewed as a cheap way to  just get more data. However our  breakthrough was not just  create more data but rather to 

**43:23**: create the right kind of data. Shape no way to teach rather  than just to fill space. This 

**43:29**: interaction between generations  of models foreshadows a  recursive set of improvement  loop were the previous 

**43:36**: generation models increasingly  helps to improve the data and  generate the training for the  next generation of models. Here 

**43:41**: at OpenAI we cracked  pretraining and reasoning and  now we are seeing their  interactions singularly 

**43:49**: deepened. In the future AI  system will move far beyond our 

**44:03**: current pretraining and  posttraining pipelines we've  been used to and we sing the  first steps towards this right 

**44:09**: now and right here. We cannot  be more excited to see what  scaling up this new set of  techniques will yield in the 

**44:15**: near future.  >> MARK CHEN: Thank you so much  and really impressive work to  both of you.

**44:21**: There is one less feature would  love to highlight which is in  help you to share this picture 

**44:26**: we have same. >> SAM ALTMAN: Thank you Mark. One of the top use cases of  Chat GPT is health. People use 

**44:32**: it a lot you've all seen  examples of people getting  day-to-day care advisor  sometimes even lifesaving 

**44:38**: diagnosis. GPT-5 is the best model ever  for health. It empowers you to  be more in control of your 

**44:43**: healthcare journey. We really prioritize improving  this forGPT-5. It scores higher 

**44:48**: than the previous model and  help bench and evaluation we  created with 250 physicians on 

**44:55**: real-world tasks. To talk about this I'd like to  invite my colleague Filipe and  his wife Carolina and to share 

**45:01**: their healthcare journey.ou  so much for joining us . >> CAROLINA MILLON: Thank you  for having us.

**45:08**: >> SAM ALTMAN: To start off can  you tell us about the journey  healthcare journey you've been 

**45:13**: on. >> CAROLINA MILLON: Yes, last  October our lives were turned  completely upside down, when I 

**45:18**: was diagnosed with three  different cancers including an  aggressive form of breast 

**45:23**: cancer. At the age of 39 all  within one week. There is just 

**45:29**: absolutely nothing that  prepares you to receive news  like this. I found out about the first 

**45:35**: diagnosis when I got an email  notification that my biopsy  results were ready. I decided 

**45:40**: to open it and when I opened it  I saw the only two words I  could understand from the 

**45:45**: report which was invasive or  Sonoma, I knew that was not  good. Everything else was just 

**45:51**: a blur of medical jargon. I  completely panicked, and in  that moment did the first thing 

**45:57**: I thought of which was to take  a screenshot of the report and  put it into Chat GPT to see if 

**46:03**: he could help me understand  what this meant? Within seconds, it translated  this complex report into plain 

**46:09**: language that I could  understand and in this moment  of overwhelmed and panic had a  little bit of clarity about 

**46:15**: what was going on. That moment  was really important because by  the time I got hold of my 

**46:21**: doctor and we got on the phone  which was three hours after I had seen the report I had a  baseline understanding of what 

**46:27**: I was facing and we were able  to jump into a conversation  about what to do next. >> SAM ALTMAN: How have you 

**46:33**: been using Chat GPT throughout  .

**46:39**: >> CAROLINA MILLON: I've used  it in so many different aspects  of my journey one of the ways I 

**46:44**: find it most powerful Ellen  helping me to make critical  decisions and help me to 

**46:49**: advocate for myself. To share an example when I was  facing a decision about whether 

**46:54**: or not to do radiation as part  of my treatment the doctors  themselves did not agree. My 

**47:01**: case was nuanced and there was  not a medical consensus on the  right path. The experts turn the decision  back to me as the patient.

**47:07**: For me bearing the weight of  this decision that could have  lifelong impact felt really 

**47:12**: heavy and I do not feel  equipped to make the call. I turned to Chat GPT to gain  knowledge and understand the 

**47:20**: nuances of my case, again  within minutes it give me a  breakdown that not only matched 

**47:38**: what the doctors had already  shared with us, but was much  more thorough than anything 

**47:43**: that could fit into a 30 minute  consultation. It would further  it help me to weigh the pros 

**47:49**: and cons, it helped me to  understand the risk and  benefits, ultimately it help me  to make a decision that I felt 

**47:56**: was informed that I felt I  could stand behind when the  stakes were so high for me and  my family.

**48:01**: >> FILIPE MILLON: For me what  was really inspirational was  watching her regain her sense  of agency by using Chat GPT in 

**48:09**: this moment it was so easy to  feel helpless to such a big 

**48:15**: dollars gap between what the  doctors know and what we know.  However no one cares more about 

**48:20**: Carolyn's help than she does  what I loved was seeing her  will empower herself and gain 

**48:25**: knowledge and become an active  participant in her own care  journey.  >> CAROLINA MILLON: I think 

**48:32**: that's a really important point  to emphasize I think the  promise of AI in healthcare is  not just in breakthrough 

**48:38**: discoveries or better  diagnostics I think it is in  creating smarter and more  empowered patients that can 

**48:47**: fully participateand advocate  for themselves and their care.  >> SAM ALTMAN: Speaking of that 

**48:53**: human testing GPT-5 what you  think. >> CAROLINA MILLON: I've been  so mind blown about GPT-5 and 

**48:58**: its capabilities. One of the  first things that jumps out at  me is how fast it is almost a 

**49:03**: little alarmingly did you think  long enough .Laughter] It is  very thorough. More importantly it feels more 

**49:09**: like a thought partner. That connects the dots. Rather than just translating 

**49:15**: information or giving you an  answer it helps you actually  navigate the problem. >> FILIPE MILLON: A great 

**49:21**: example we went back and took  our initial biopsy prompts and 

**49:26**: put them into GPT-5 GPT-4o did  a great job it translated  explained what these words 

**49:31**: meant and helped in a way we  can understand but GPT-5 seem  to understand more of the 

**49:39**: context and the question behind  the question but why would we  ask about biopsy results? Here is what is not on here 

**49:44**: here is what results are  pending picture of desk about  your questions you might want  to ask your doctor and think 

**49:51**: when you start talking to them.  It really start to pull  together a complete 

**49:57**: personalized picture. That is what really inspires us  you can see all of the amazing 

**50:02**: improvements in the benchmarks  but what is so helpful is this 

**50:11**: tool is available today. The  reason Carolina and I are here  at the reason we's feel so  passionate about sharing her 

**50:17**: story is for that individual  that will get a diagnosis with  this today those families going 

**50:23**: through cancer diagnosis  similar to medical diagnosis  will be some of the most 

**50:29**: challenging decisions of their  lives. What really inspires me  is that they will have access  to better tools and support 

**50:35**: then we had even just eight  months ago. >> SAM ALTMAN: We are  incredibly excited for that 

**50:40**: thank you so much for sharing  your story we are pleased that  BTT will be helpful to you we  hope the new version can help a 

**50:47**: lot of people we wish you the  very best I'd like to hand it  over to our president Greg 

**50:52**: Brockman. >> GREG BROCKMAN: [Applause]. Software engineering is already 

**50:58**: fundamentally changing. GPT-5  will turbocharge that  revolution. We released our first coding 

**51:04**: optimized model back in 2021  and demonstrated 11 stream much  like this one what we would 

**51:09**: call vibe coding today for the  very first time. Talk to the model and ask it 

**51:15**: for a little application a  little game of feature in a  game he would actually do it I  remember seeing the model 

**51:24**: incapable of doing this it was  so mind blowing you realize we  have to see where this goes.  This is the promise of what 

**51:30**: computers can be you could talk  to them and actually do what  you want. They can fully  amplify what you are able to 

**51:37**: accomplish and what you're able  to deliver to not just your own  benefit but really for the 

**51:42**: world. This year we policed great  coding models like GPT-4o and  o3 but GPT-5 says whole new 

**51:47**: standard. It is the best model at Agentic  coding tasks. You can ask it to  go in a couple or something 

**51:53**: very complicated I will will go 

**52:05**: off and work on it it will call  many tools to work for many  minutes at a time sometimes 

**52:10**: even longer. To accomplish your  goal. Your instruction your 

**52:16**: task. Whatever it is you're  trying to build. It's  incredible at front and makes  very beautiful visualization 

**52:21**: and interactive games and you  seen some of this in the live  stream so far you'll see some 

**52:27**: more upcoming. It is really  amazing to see whatever you  imagine coming to life. It's extremely good at 

**52:33**: instruction following very  detailed instructions. In able to accomplish when you 

**52:38**: have something very vaguely  specified inferring your intent  or something detail specify 

**52:44**: actually following it. It's also very fast  encompassing these task again  it takes the right amount 

**52:49**: accomplish which of interview  we are making it available not  just to developers to use to 

**52:55**: write their own code but the  build novel applications. We  are putting into the API to 

**53:00**: talk but that is Michelle.  >> MICHELLE POKRASS: Thank you  Craig I'm Michelle I lead the  research team and post training 

**53:06**: focused on improving our models  for our users that includes use  cases like instruction 

**53:12**: following and coding. Today I'm  so sad to tell you that we are  shipping three state-of-the-art 

**53:18**: recent models in the API.  GPT-5, GPT-5 mini and GPT-5  nano all three stopped writing 

**53:24**: in the cost latency curve so  you can pick the right one for  your application. We also for the first time 

**53:29**: releasing a new perimeter  option for reasoning effort  called minimal. This is so you 

**53:34**: can use these reasoning models  but with minimal reasoning so  they can slot into the very  fast and most latency sensitive 

**53:43**: applications. Now you don't  actually need to choose between  a bunch of models and can use  GPT-5 for all of your use cases 

**53:49**: and just dial in the reasoning  effort. We also have a few new features  coming to the API. The first is 

**53:54**: called custom tools. In the past all of our function  calling had the model rockets  are put in JSON this works very 

**54:01**: well when the model needs to  put a few parameters but  sometimes developers are  pushing our models to their 

**54:07**: limits and that they have  extremely long arguments for  tool calls. It can be more challenging for 

**54:13**: the models to escape valid  control characters out of 100  lines of code in JSON that is 

**54:19**: why custom tools are just  free-form plaintext what is  typical is we are releasing an  extension to structured outputs 

**54:25**: or you can supply a regular  expression or even a context  free grammar and constrain the 

**54:30**: model's output to that. This  will be super useful if you  want to supply a custom DSL if  you have your own SQL for it 

**54:36**: specified the model always  follow that format.e also  shipping tool call preambles. 

**54:41**: This is the model's ability to  output explanation of what it  is about to do before it calls 

**54:46**: the tools. This is not super  new but o3 did not have this 

**54:59**: capability in GPT-5 it is  supercharged with extreme  durability. The model is able  to follow instructions about 

**55:07**: these preambles very  effectively. You can ask the  model to give a preamble before  every tool call or only when 

**55:13**: something notable is going to  happen or not at all. Next we  are shipping a verbosity 

**55:18**: programmer we wanted this in  the API for a long time now you  can set verbosity to low medium 

**55:24**: and high to control how terse  or expansive the model is with  its output. GPT-5 is a state-of-the-art 

**55:29**: coding model. On SWEBench it measure a Python  coding ability GPT-5 says new  high of 74.9% versus the 69.1% 

**55:36**: from o3. On Aider Polyglot  which is a benchmark that  covers all sorts of programming  images and noxious Python GPT-5 

**55:42**: scores 88% stark improvement  over o3. He also have seen it's  incredible at front end web 

**55:47**: development we vest human  trainers to look at outputs for  GPT-5 in o3 and pick which they 

**55:54**: prefer they preferred GPT-5 70%  of the time. For its improved  aesthetic ability but also 

**55:59**: better capabilities overall.  GPT-5 is not just for coding.  It's incredible at Agentic tool 

**56:06**: call in. It is the leading  state-of-the-art model for tool  call and we see this on the new 

**56:12**: tower square benchmark this  benchmark the least just two  months ago is a test of the 

**56:17**: model's ability to call tools  and work in concert with the  user to solve a challenging  problem this case in the 

**56:23**: telecom industry trying to  solve the ability problem for a  user not having the service 

**56:30**: working. Just two months ago no  model in the field score more  than 49% and today TBD five 

**56:35**: scores 97%. GPT-5 is also state-of-the-art  on general-purpose instruction 

**56:40**: following. It scores 99% on COLLIE which 

**56:59**: signals a great departure from  this benchmark for us. It also  scores 70% on scales with a 

**57:04**: challenge benchmark up 10  points from all three. This is  a measure of multiturn  instruction following. Finally 

**57:11**: the instruction following  prefer the most is when we  built in-house. It is based on 

**57:16**: real API use cases for that  reason it's really good measure  of how GPT-5 will perform in  your application. On the hard 

**57:22**: subset of this GPT-5 scores 64%  up from 40% from all three 

**57:42**: pretty meaningful improvement  we think it will perform quite  well in your applications. We 

**57:48**: also bring GPT-5 to a longer  context window in the API. It  is now that 400 K of total  context up from 200 K from all 

**57:55**: three it's not enough to just  release over context window we  want to make it more effective  and usable. GPT-5 is 

**58:01**: state-of-the-art on 128K and  258K of OpenAI MRCR which is  benchmark we open source too  much to go along context 

**58:07**: capability it state-of-the-art  on OpenAI graphwalks BFS  benchmark which is a measure of 

**58:13**: the model's ability to reason  overflow context inputs. It's a great merger of the  risen capabilities and also the 

**58:20**: longer context in this model.  We also open sourcing a new  loan context eval called rows  comp loan context to measure 

**58:26**: the model's ability to answer  challenging questions over one  context. We are sent to spur on 

**58:32**: work in this field.e think  GPT-5 is the best model for  developers. It was trained with a focus on 

**58:38**: real-world utility and less on  benchmarks but we happen to  pick up a few of those along  the way.

**58:43**: We focus a lot on the  intersection of engineering and  research we think you will  really love working with this 

**58:49**: model. [Music]. >> GREG BROCKMAN: Thank you  Michelle.As Michelle was 

**58:55**: saying the benchmarks they are  exciting members.

**59:01**: We are starting to saturate  them when you move between 

**59:11**: 9899% it means you mean  something else to Target the  model is one thing we've done 

**59:16**: for differently with this model  is really focus on not just  these numbers but really on 

**59:23**: real-world application being  releasable to you in your daily  workflow. Hearing about it is  much less exciting to sing it 

**59:29**: to show this model in action  I'd like to welcome ADI and  Brian to the stage. >> ADI GANESH: Thank you Greg.

**59:36**: >> BRIAN FIOCA: I'm Brian a  solutions architect in the  startup team. >> ADI GANESH: I'm ADI a 

**59:42**: researcher and bowstring Tim. >> BRIAN FIOCA: To create the  ideal per program NIDA model 

**59:47**: that understands the software  engineering practices but has a  personality that feels right to 

**59:53**: work with. For GPT-5 we worked  really hard to make the model  appear perfectly with you by  default out of the box.

**1:00:01**: Let me pull up a demo of GPT-5  inside of Cursor to show you  this behavior retarded.

**1:00:08**: Last month I was on a different  live stream towards the end I  ran into a bug that I covered 

**1:00:13**: up after wards I try to have  GPT-5 I tried to have all three  fix it for me and it couldn't. While we were testing GPT-5 

**1:00:21**: before this had it see if he  could fix that but for me to  taunt the demo God will see if 

**1:00:27**: can do it on stage. Let's hope for better luck in  o3.

**1:00:36**: >> BRIAN FIOCA: This is less  about the fix and more about  the beaver of the model during  this process right up front you 

**1:00:44**: will see it will tell you it's  plan it will tell you how it  will look for the bug maybe how 

**1:00:49**: it will fix it this kind of  communication shows builds  trust during a coding session  helps you to re-track if you

**1:00:56**: need to but you don't need to.  It's . >> ADI GANESH: I like how it  gives you updates it said was 

**1:01:01**: search then continues. >> BRIAN FIOCA: It searches  faster than me it is using the 

**1:01:07**: same best practices I use when  writing this down but is much  more peril than Iam as a  developer. 

**1:01:13**: >> SEBASTIEN BUBECK: Did you  try to fix the bug yourself . >> BRIAN FIOCA: I did and it  couldn't do it.

**1:01:19**: [Laughter] I was busy. [Laughter] Continuing on is  like starting to figure out 

**1:01:24**: where it is going it is going  to sort of get this out while  this is going let me tell you 

**1:01:29**: little bit about how we trained  GPT-5 to behave this way. We started by talking to users 

**1:01:34**: and customers about how our  models perform in the most  popular coding tools like  Cursor and we identified 

**1:01:40**: frustrations and rough edges  and boiled it all down into  four personality traits.

**1:01:46**: utonomy, collaboration and  communication context  management and testing.

**1:01:55**: We turn those into a rubric  that we used to shape the  models behavior then we tuned  it in till it felt like a 

**1:02:00**: collaborative teammate while we  were using it. >> GREG BROCKMAN: It is been 

**1:02:05**: really amazing to see the team  doing the grant of going to see  how this model behaves in 

**1:02:10**: practice going out with people  really wantand putting that  back into the model training  think that is something that is 

**1:02:17**: been a real focus for this  model.  >> ADI GANESH: It's been pretty  great .

**1:02:22**: >> BRIAN FIOCA: While this is  fixing the other thing we did  during testing we were pressed 

**1:02:27**: for time we had to factor  whatever test harnesses to run  parallel on Dr. and set it off 

**1:02:33**: came back like 45 minutes later  like it just finished. We  tested it out and it ran the 

**1:02:38**: first time. It was pretty surprising. >> GREG BROCKMAN: That is  magical. >> BRIAN FIOCA: It made the  edits it found the right 

**1:02:45**: problem. Right now it is actually it is  running lints but these lints  are actually not related to 

**1:02:50**: this bug is going to ignore  them. It is going to run a build it 

**1:02:56**: will run test if there are any. It will make sure that this  code is shippable before it is 

**1:03:01**: done. >> ADI GANESH: It is really  smart find lints and it  realizes it is not relevant to 

**1:03:07**: the specific bug we are fixing  is not making unnecessary  edits. 

**1:03:13**: >> BRIAN FIOCA: Totally this is 

**1:03:21**: one example that shows the  power of the autonomy and the  collaborative communication and 

**1:03:26**: help he stays pliable on  difficult coding tasks without  getting stuck on death loops.

**1:03:32**: The best part GPT-5 is totally  tunable you can steer it with  system or Cursor rules you can 

**1:03:37**: change its verbosity levels or  missing levels to match your  task. If you get stuck ask it, 

**1:03:42**: GPT-5 is actually really good  at modifying its own prompts by  meta-prompting after using this 

**1:03:49**: for the past few weeks it  really feels like we achieved  state-of-the-art zero shop 

**1:03:54**: performance and reliability  across the most complex coding 

**1:04:00**: tasks. For me it's the first  time I trust a model to do my  most important work. This is 

**1:04:05**: beyond vibe coding is  incredibly powerful tool and  I'm really excited for people  to try it.

**1:04:15**: >> ADI GANESH: It super excited  to see a part GPT-5 it has come 

**1:04:31**: when it comes to coding  personality and steerability  I'm really excited to show how  great GPT-5 is it front-end 

**1:04:37**: coding which is not an ecstatic  swirly matter of attitude demos  for you today. One, for work 

**1:04:44**: and one for fun. Let's start  with the work example. Imagine you are the CFO of a  startup company have some data 

**1:04:49**: I would like to visualize about  the company. I will ask the model to make me  a dashboard.

**1:04:56**: You'll see here that I'm being  specific about the audience so  the target audience is the CFO, 

**1:05:01**: create a finance dashboard for  my startup. I've asked it to be beautiful, 

**1:05:07**: tastefully designed with some  interactivity, and to have a  clear hierarchy for easy focus 

**1:05:13**: on what matters. I've also  specified what framework it  should use. You can see that it 

**1:05:18**: is actually started it's  following my instructions and  using create next app to make 

**1:05:23**: an SJSproject. >> BRIAN FIOCA: Totally from  scratch .

**1:05:28**: >> GREG BROCKMAN: How long do  you think the task would take  you to do.  >> ADI GANESH: At least a 

**1:05:34**: couple of days and not upfront  and expert just understand  latest would easily take me a  few days.

**1:05:40**: >> GREG BROCKMAN: Will see how  long it takes with the model.  >> ADI GANESH: 19 it's really 

**1:05:45**: cool to see the model has  fought for but it'll explain  how it will structure the  product it talks how we will 

**1:05:53**: scaffold the elusive tailwinds  CSS. It's running a couple of  commands to install  dependencies.

**1:05:58**: Which is cool. Now it is proceeding to  implement the rest of the  project. While this runs I will 

**1:06:03**: talk a little about how we  train GPT-5 to be a great  front-end coding model. We 

**1:06:08**: tried to follow the principle  of giving it good estimates by  default. But also making it  steerable.

**1:06:14**: If I give the model a concise  prompt it should be able to 

**1:06:26**: infer my intent to make  something that looks great by  default. On the other hand if  I'm specific about a layout or 

**1:06:32**: framework I want the model to  use it to follow my  instructions precisely. This  makes it the best of both 

**1:06:40**: worlds for developers. We also trained GPT-5 to be  much more Agentic than previous 

**1:06:45**: models. If you give it a task  like this it will run long  chains of reasoning and tool 

**1:06:51**: calls just go to work. The  build code that is both  ambitious and coherent. >> BRIAN FIOCA: Like who said 

**1:06:57**: ambitious it means it goes  above and beyond without going  off track all of which are  specified.

**1:07:04**: >> ADI GANESH: What we want is  a model should adhere to my  prompt but also be ambitious  and go above and beyond when it 

**1:07:09**: thinks it can. So checking in here looks like  the model is making progress it  is creating a readme file.

**1:07:16**: I think it is thinking about  how to make the code module or  it is created like a bar chart  component it looks like it is 

**1:07:22**: continuing here. >> GREG BROCKMAN: Love it does  not just write the code thinks  about Opera abstractions and 

**1:07:28**: acutation the whole life cycle  of what it is to write  software.  >> ADI GANESH: Exactly it is 

**1:07:34**: not just write the code like in  SWEBench it is all  communicating about the code  and explaining what it is 

**1:07:41**: doing. While this runs GPT-5 

**1:08:05**: understands the details much  better than previous models.  When we trained the model we 

**1:08:10**: taught it to understand details  like typography color and  spacing. In a way that just  coaxes any previous model we 

**1:08:16**: have shown. I remember with the  old mouse would have to write  really specific prompts to get 

**1:08:21**: it to do what you want. But  GPT-5 just gives yougreat 

**1:08:28**: results by default. >> BRIAN FIOCA: During testing  relocate H and B for different  versions of the model to see if 

**1:08:34**: he was doing better atUI at  some point we stopped being  able to tell and with appellant  designers to teach us what is 

**1:08:41**: better. >> ADI GANESH: It was  fascinating to see the ball  specific performance during  training we woke up one day and 

**1:08:47**: it was making these great UIs . >> GREG BROCKMAN: How did the  models static preferences  compare to your own .

**1:08:53**: >> ADI GANESH: I think in  general I feel the model has  better aesthetics than me. 

**1:08:59**: Usually I defer to its  judgment. I find that like really helpful  when trying to make it up not 

**1:09:05**: sure how one to look at the  model defaults are just great. Checking in here. You can see 

**1:09:10**: that the model has actually  structured the code into the  different components. It is 

**1:09:16**: made a simple data type script  file KPI card component revenue  chart. Like I said it is super modular  it is thinking about how to 

**1:09:22**: adjust write code but right  high-quality code that can  actually be merged. >> BRIAN FIOCA: I feel like it 

**1:09:30**: is close. > ADI GANESH: I think it is  pretty close. >> BRIAN FIOCA: You did say  ambitious.

**1:09:35**: >> ADI GANESH: [Laughter] This  is awesome. You can see here is 

**1:09:41**: actually building the project  and instrument errors back to  itself. This is just a profound moment 

**1:09:46**: to see the model could write  code but also one bills and  stream the errors back and  iterate on the code. It is able 

**1:09:53**: to improve its own code in this  sort ofself-improvement loop 

**1:09:59**: which is fascinating. >> GREG BROCKMAN: It is  definitely a good taste of what  the future holds as well when 

**1:10:05**: you think about where these  models can go and how much they  can accelerate developers on 

**1:10:10**: all aspects of what we all  collectively do.  >> ADI GANESH: Exactly ! > BRIAN FIOCA: It just fixed 

**1:10:17**: a bug is found in the previous  build. >> ADI GANESH: It looks like is  done let's check it out. 

**1:10:23**: will follow the instructions  that I don't really know front  end. Let me see how I should  run it. It says CP to the directory 

**1:10:29**: then looks like it served on  port 3001 when he opened that  port. >> GREG BROCKMAN: It is alive. 

**1:10:35**: >> ADI GANESH: You can see here  let's check it out. The model  has maybe a dashboard it is 

**1:10:41**: telling me my AR cash looks 

**1:10:53**: like this company is doing well  even see revenue is growing.  The model has added some 

**1:10:58**: interactivity here. If I hover  over a graph it actually tells  me the exact value for a 

**1:11:03**: particular day it would take me  five hours to do that in D3.

**1:11:14**: >> GREG BROCKMAN: Just because  it is easy to take this for  granted can you remind the  audience with the actual prompt 

**1:11:21**: was how much creativity and  understanding your intent was  required to compress this. >> ADI GANESH: It is crazy 

**1:11:26**: that this prompt is so concise  it is able to just give you  something to looks beautiful in 

**1:11:31**: just five minutes. >> GREG BROCKMAN: That is  amazing.  >> ADI GANESH: It is also  implemented another graph here 

**1:11:38**: showing our customers. It is  also implemented a date picker  so Ican filter by different 

**1:11:43**: dates and visualize data  accordingly. It is even sort of segmented it  by customer segment which is 

**1:11:49**: cool. This is just one example that  highlights the power of GPT-5 . >> GREG BROCKMAN: There will no 

**1:11:56**: longer be an excuse for ugly  internal applications. >> ADI GANESH: [Laughter] Let's  go to the fun demo. 

**1:12:02**: > GREG BROCKMAN: This was  pretty fun but even more. >> ADI GANESH: I have a younger  cousin and I want to make a 

**1:12:08**: game for her. I want to make a  3D game that incorporates a  castle so you can see my prompt 

**1:12:13**: I will kick this off . >> GREG BROCKMAN: It is always  the non-áUNTRAN1á parts.

**1:12:20**: >> ADI GANESH: You can see my  prompt.

**1:12:33**: Create a beautiful castle  included some details like we  want people patrolling the 

**1:12:38**: walls some movement horses, I  want a minigame where American  pop balloons by clicking on 

**1:12:43**: them. This should make a sound  effect. Let me run the spread  in cursor. I go to show an example I've 

**1:12:49**: already generated just to save  some time. Here is the beautiful castle  the model made.

**1:12:55**: It is just filed how from a  concise prompt the model has  this great sense of aesthetics 

**1:13:00**: where it is made this floating  rock, made a 3D castle if you  zoom in you can see tons of  detail. These guards walking 

**1:13:07**: around cannons firing you want  to fire the cannons? >> BRIAN FIOCA: Of course. [Laughter] 

**1:13:16**: >> GREG BROCKMAN: Who would not  want to.  >> ADI GANESH: Dared to go you  can part the cannons you can 

**1:13:22**: even chat with the characters  will sayhi to Capt. Rowen.  >> BRIAN FIOCA: They have names  . > ADI GANESH: Say hello to 

**1:13:28**: the merchant. The merchant is  selling some stuff. What is your favorite song? A pallet of banners and dogs.

**1:13:35**: Give me some wisdom? Curiosity is volatile. That makes sense.

**1:13:44**: >> BRIAN FIOCA: The minigame. >> ADI GANESH: Do wantto try to  minigame. >> GREG BROCKMAN: Let's play 

**1:13:50**: the minigame . >> ADI GANESH: You want to try  it Greg you can fire at these  balloons.

**1:13:55**: >> GREG BROCKMAN: Oh no I'm not  good at it maybe I can ask  GPT-5 for help with it.

**1:14:01**: I got one there we go pick out  a sound effect. >> ADI GANESH: These are 

**1:14:08**: historically accurate balloons. [Laughter]. >> GREG BROCKMAN: Did I get a 

**1:14:13**: second one this game is harder  than it looks hold on we have a  balloon coming. [Laughter] There we go.

**1:14:19**: I think I should quit while I'm  ahead. >> ADI GANESH: Working with  GPT-5 has been really fun and 

**1:14:33**: profound for me because for me  this is the first model I've  worked with that actually has a  sense of creativity. We are 

**1:14:40**: really excited to see how GPT-5  unlocks your creativity. >> GREG BROCKMAN: Thank you 

**1:14:45**: both this is absolutely  amazing. Now we believe that Judy five  is the best coding model in the 

**1:14:53**: world. Don't just hear it from us to  talk more about this model and  how to make it really useful 

**1:15:01**: for developers I like to  welcome Michael Truell with the  cofounder and CEO of cursor. >> MICHAEL TRUELL: Thank you 

**1:15:09**: good to be here. >> GREG BROCKMAN: Great to have  you. What was your very first  expense with GPT-5. >> MICHAEL TRUELL: When we get 

**1:15:16**: access to GPT-5 we used it on  her actual work and so to start  with as a task we tested to  tell us something not obvious 

**1:15:23**: about our code base. Within a  couple of minutes it peered  into the code base it edified a 

**1:15:29**: particular system we use for 

**1:15:48**: remote code execution it  identified a nonobvious  architecture decision we made.  Bennett also understood why we 

**1:15:55**: made that architecture  decision. It was to harden our  security. Those were 

**1:16:00**: architecture decisions and  trade-offs that took humans  weeks to think through. It is  kind of amazing to see its code 

**1:16:07**: base understanding abilities  from the-  >> GREG BROCKMAN: That is  really great not just the code 

**1:16:13**: writing but the reading and  understanding turns out there  is so much for the support and 

**1:16:18**: just the emitting of the code. >> MICHAEL TRUELL: The  understanding is an important 

**1:16:24**: prerequisite. >> GREG BROCKMAN: What stood  out most to about GPT-5. >> MICHAEL TRUELL: Is a very 

**1:16:29**: smart model.ntil it is  marked it does not compromise 

**1:16:36**: on its ease-of-use. Four bill  per programming that means it's  incurably fast. That also means 

**1:16:43**: is quite interactive. It is good about talking about  what it is about to do breaking 

**1:16:48**: problems down into sub problems  that human can then see. Living  a reason trace you can then 

**1:16:53**: intervene on and react to. It's  also great not just that you  give it one initial query and a 

**1:16:59**: ghost does that but working  with you over a long session.  Where you are asking to  backtrack on something that is 

**1:17:05**: gone down or asking it to make  additional changes to the code  base. 

**1:17:11**: >> GREG BROCKMAN: Should we  show it in action.  >> MICHAEL TRUELL: Let's do it  I think we are going to go and 

**1:17:17**: will try and sell the bond this  is the OpenAI Python SDK there  are bunch of issues with the  OpenAI Python SDK there are 

**1:17:24**: also a lot of close issues.  Seems like there's a problem  with uploading PS through the  SDK. 

**1:17:29**: > GREG BROCKMAN: This is  been open for three weeks it is  not a trivial problem. 

**1:17:34**: >> MICHAEL TRUELL: Let's see if  we tackled this issue we will  go and take the issue will 

**1:17:40**: paste into the Cursor GPT-5  will set up and try to solve 

**1:17:46**: the problem this is an example  of the robustness of the model  in the API. We are to solve the  problem in Cursor it is working 

**1:17:52**: with a set of custom models it  is not seen before a set of  custom tools it is not seen 

**1:17:57**: before to do things like pull  down text from the web to  search brought the CodeBase 

**1:18:02**: it's incredibly robust and  adept at using those tools. And it boosts the eval results. 

**1:18:08**: >> BRIAN FIOCA: Loved seeing  the explosion all the things it  is running it through how this 

**1:18:14**: is compared to how you would  solve this problem. >> MICHAEL TRUELL: Is very  fast.

**1:18:19**: You can see it's made a  high-level plan search brought  the CodeBase is started to read  some files.nd continued 

**1:18:25**: searching now it is thinking  through what it would like to  do next. Now it started to actually 

**1:18:30**: solve the issue. Started to think through some  coded changes. >> GREG BROCKMAN: Any advice 

**1:18:36**: for people and how to get the  most of GPT-5 in Cursor? >> MICHAEL TRUELL: I would 

**1:18:41**: suggest using it for your real  work. GPT-5 is a step forward towards  real power programmer start

**1:18:46**: using as a helper on daily  driver model for you. If you have not used AI to code  much before I would take some 

**1:18:52**: of your more scope down  problems and try handing them  off to the bot and working with  it synchronously. Spacing think 

**1:18:59**: the fact that GPT-5 is so great  for the real world big coal  bases not a demo of one of 

**1:19:04**: application is cool is that is  the real folly comes from fully  operating in alarger CodeBase .

**1:19:10**: > MICHAEL TRUELL: Definitely  it's CodeBase understanding is  impressive in its ability to be 

**1:19:16**: stupid is impressive if you  specify a long complicated task  with lots of subtleties in the 

**1:19:22**: initial instructions it is very  good at picking up the  subtleties it's also very good 

**1:19:28**: at if it is gone down a wrong  path and he goes and exceed the  code or his back from you it  was incorrect it is good at 

**1:19:35**: backtracking . >> GREG BROCKMAN: What can't  GPT-5 do? >> MICHAEL TRUELL: We are 

**1:19:40**: really excited about computer  using capabilities about that  getting better it would be 

**1:19:45**: great if for instance the  dashboard if he can run the  code see the output QA every  little bit itself then react to 

**1:19:52**: it. Looking forward to computer  using capability how would you  like to be five to be better?

**1:19:58**: >> GREG BROCKMAN: I think  that's a great one expanding  the dimensions I think it is in  all direction there so much 

**1:20:07**: like doing dev ops and other  work that is external to  software code writing as we  think of it today. But also you look at these 

**1:20:14**: demos weave from them for five  minutes or 10 minutes a couple  of hours I think extending that 

**1:20:19**: lifecycle to really be able to  go for days and weeks  eventually even months I think  that is ultimately where we 

**1:20:25**: expect things to go. >> MICHAEL TRUELL: We can see  it peered into the CodeBase  discovered that there is an 

**1:20:31**: issue with the MMMU sent out  for PDFs and the plumbing  through the SDK. It identified  that hestarted making some 

**1:20:38**: coded changes. It created some new methods it  can edit an existing code this  looks roughly correct.

**1:20:44**: I would love to merchandise the  PR to burn  >> FILIPE MILLON: I would love  to do that as well let's do 

**1:20:50**: that after the show that you so  much we are so excited to have  GPT-5 in Cursor and starting 

**1:20:55**: today . >> MICHAEL TRUELL: I'm excited  to partner with you guys  starting today GPT-5 is default 

**1:21:01**: for new users in Cursor we are  releasing it all Cursor users  to try for the next few days so 

**1:21:06**: people get a sense of the model  is the smartest coding model be  retried.  >> GREG BROCKMAN: Awesome thank 

**1:21:12**: you so much Michael. [Applause]. [Unclear Audio] we think of it  like it's great for the 

**1:21:18**: enterprise we think of it like  a subject matter expert that is  in your pocket that is an 

**1:21:23**: expert across every domain.  Legal finance whatever  application you have in mind.  To talk about how to be five 

**1:21:29**: can be applied to the  enterprise and like to welcome  Olivier to the stage. >> OLIVIER GODEMENT: Thank you 

**1:21:35**: Greg hello everyone I'm Olivier  lead the platform at OpenAI. At  this point I think you got the 

**1:21:41**: message we care a ton about  developers including but that 

**1:21:47**: is not all enabling businesses  and governments it's critical  to OpenAI mission. We want to enable the key 

**1:21:53**: industries to transform  themselves such as healthcare  education energy and finance.  Since we know Chat GPT and API 

**1:22:00**: 5 million businesses has been  using our technology I'm still  mind blown 5 million 

**1:22:05**: businesses. Those businesses  are not just playing they just  not X permitting the air 

**1:22:10**: pushing in production new  products in the real world. I  believe GPT-5 is going to be a 

**1:22:16**: step function . As Sam  mentioned earlier the having a  subject matter expert in your 

**1:22:21**: pocket will be enable every 

**1:22:27**: employee to do more limit to be  up through examples. First want  to talk about life sciences.

**1:22:33**: Amgen is a company in the US  that designed new drugs new  medicines to fight some of the 

**1:22:38**: toughest human diseases. Amgen  was one of the first testers of  GPT-5. They used it in the  context of drug design. What 

**1:22:46**: Amgen centers found is GPT-5 is  actually good at deep reasoning 

**1:22:53**: with complex data. Think  analyzing scientifical  literature or clinical data.

**1:23:02**: Next want to talk about  finance. BBVA is a  multinational bank which is  headquartered in Madrid in 

**1:23:08**: Spain BBVA been using GPT-5 for  financial analysis. The Takeaway was pretty clear 

**1:23:13**: GPT-5 beats every single other  model out there in terms of  accuracy and speed. What used  to take three weeks from a 

**1:23:19**: financial analysis to do GPT-5  can do it in a couple of hours.  Next I want to talk about 

**1:23:24**: healthcare. Oscar Health is an insurance  company based in New York  they've been using GPT-5 what 

**1:23:31**: they found GPT-5 is a single  best model for clinical  reasoning think complex medical 

**1:23:36**: policy to patient's conditions. It is not all businesses it's  also about government we are 

**1:23:42**: super excited the announcement  we made yesterday that the 2  million US federal employees 

**1:23:48**: will be able to use GPT-5 and  Chat GPT cannot wait to see how 

**1:23:53**: that enables to develop better  better services to the American  people. Wrinkly that is very cool I 

**1:23:59**: think that is the tip of the  iceberg.

**1:24:04**: If history is a teacher and  we've seen it with GPT-4o we  are going to see many many use  cases in a merge all of us 

**1:24:10**: cannot imagine I cannot wait  for us to go in that adventure 

**1:24:23**: together let's talk about  pricing and availability GPT-5  is going to be available in the 

**1:24:29**: API starting today. Three  models GPT-5, GPT-5 mini, GPT-5  nano. GPT-5 will be priced at  $1.25 at 1 million input tone 

**1:24:35**: many and none are faster GPT-5  nano is 25 times more 

**1:24:41**: affordable for GPT-5 it's  vertical. I cannot wait to see  what you will build next I will 

**1:24:47**: keep scientific Jakub will  close us out. [Applause].  >> JAKUB PACHOCKI: Thank you at 

**1:24:55**: OpenAI we are about  understanding this miraculous 

**1:25:02**: technology. Called deep learning. What its consequences are?

**1:25:09**: Our research aims to understand  what deep learning is capable  of and how to steer it to make  it safe and useful for all of 

**1:25:17**: us.

**1:25:22**: This is a work of passion. And it is a mission. I want to recognize and just 

**1:25:33**: deeply thank the team at  OpenAI.

**1:25:41**: It is a great privilege.  [Applause].

**1:25:48**: It is great privilege for me to  work alongside this incredible  group of brilliant people 

**1:25:56**: driven by theshared goal , what 

**1:26:07**: happens to model activity five  years of investigation not only  at producing a great release 

**1:26:13**: but at building understanding  of this underlying technology  itself. A lot of what you will see in 

**1:26:19**: that this model is really just  really glances of new ideas.

**1:26:25**: That we believe will go much  further.

**1:26:31**: There is a lot we still have to  understand, we look towards the  future where AI can uncover 

**1:26:37**: knowledge about the world and  meaningfully transform our  lives for the better.

**1:26:44**: We hope you enjoy what we built  and we will get back toscaling 

**1:26:53**: . Thank you. [Applause].

**1:27:03**: [Music].

