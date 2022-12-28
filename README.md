# metatrader_pyscript
This python code allow you to execute Metatrader scripts. It is usefull to remotely control your trading actions, you can integrate it for example with telegram, so you can build a bot that close all open orders for emergency.

<h2>Preparing</h2>
<p>Install the script that you want to run on Metatrader (I tested with "Close all open orders"). After that, set an hotkey for it, in my case I setted "alt" + "c".</p>
<p>Inside the file, change the number at the bottom of the code with your actual string. It is the start of the name of the Metatrader's window, in my case, using Metatrader provided by FxPro, it is the account id. This part of the code is used to select the correct window were the script will run the hotkey. In my case the name of the window change changing a graph, but the start of the window name remain the account id, so I can't do mistakes with this solution.</p>
<p>At the end of the code, set your current hotkey desired</p>
