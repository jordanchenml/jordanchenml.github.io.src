Title: Statistics Questions in Interview
Date: 2020-03-17 13:40
Category: Interview
Tags: Statistics, Mathematical
Slug: Statistics Questions in Interview
Author: Jordan Chen
Summary: Detailed answers to statistical questions in the interview

# <center>Statistics Answers</center>

## 1.

There are 5 situations when taking 4 balls from the box.

① 4 red balls.
$$
P(4\ red) = \frac{5}{10} \times \frac{4}{9} \times \frac{3}{8} \times \frac{2}{7}
$$
② 1 white ball and 3 red balls.
$$
P(1\ white\ and\ 3\ red) = \frac{5}{10} \times \frac{5}{9} \times \frac{4}{8} \times \frac{3}{7}
$$
③ 2 white ball and 2 red balls.
$$
P(2\ white\ and\ 2\ red) = \frac{5}{10} \times \frac{4}{9} \times \frac{5}{8} \times \frac{4}{7}
$$
④ 3 white ball and 1 red balls.
$$
P(3\ white\ and\ 1\ red) = \frac{5}{10} \times \frac{4}{9} \times \frac{3}{8} \times \frac{5}{7}
$$
⑤ 4 white balls.
$$
P(4\ white) = \frac{5}{10} \times \frac{4}{9} \times \frac{3}{8} \times \frac{2}{7}
$$




Expected value:
$$
\begin{equation}
\begin{aligned}
E(\left|Number_{white} - Number_{red}  \right|) &= 4 \times [P(4\ red) + P(4\ white)] \\
&\ \ \ \ + 2 \times [P(1\ white\ and\ 3\ red) + P(3\ white\ and\ 1\ red)] \\
&\ \ \ \ + 0 \times P(2\ white\ and\ 2\ red) \\
&= 4 \times \frac{120 \times 2}{5040} + 2 \times \frac{300 \times 2}{5040} + 0 \\
&= \frac{2160}{5040} \\
&= \frac{3}{7}
\end{aligned}
\end{equation}
$$












## 2.

The probability of the number of white and red balls in the box is a $Binomial\ Distribution$.

There are 11 combinations in the box, below are their probabilities:
$$
\begin{equation}
\begin{aligned}
P(0\ white+10\ red) &= \begin{pmatrix} 10\\0 \end{pmatrix}\times (\frac{1}{2})^0\times (\frac{1}{2})^{10} = \frac{1}{1024},\ \ \ P(10\ white+0\ red) = \begin{pmatrix} 10\\10 \end{pmatrix}\times (\frac{1}{2})^{10}\times (\frac{1}{2})^0 = \frac{1}{1024}\\
P(1\ white+9\ red) &= \begin{pmatrix} 10\\1 \end{pmatrix}\times (\frac{1}{2})^1\times (\frac{1}{2})^9 = \frac{10}{1024},\ \ \ \ P(9\ white+1\ red) = \begin{pmatrix} 10\\9 \end{pmatrix}\times (\frac{1}{2})^9\times (\frac{1}{2})^1 = \frac{10}{1024}\\
P(2\ white+8\ red) &= \begin{pmatrix} 10\\2 \end{pmatrix}\times (\frac{1}{2})^2\times (\frac{1}{2})^8 = \frac{45}{1024},\ \ \ \ P(8\ white+2\ red) = \begin{pmatrix} 10\\8 \end{pmatrix}\times (\frac{1}{2})^8\times (\frac{1}{2})^2 = \frac{45}{1024}\\
P(3\ white+7\ red) &= \begin{pmatrix} 10\\3 \end{pmatrix}\times (\frac{1}{2})^3\times (\frac{1}{2})^7 = \frac{120}{1024},\ \ \ \ P(7\ white+3\ red) = \begin{pmatrix} 10\\7 \end{pmatrix}\times (\frac{1}{2})^7\times (\frac{1}{2})^3 = \frac{120}{1024}\\
P(4\ white+6\ red) &= \begin{pmatrix} 10\\4 \end{pmatrix}\times (\frac{1}{2})^4\times (\frac{1}{2})^6 = \frac{210}{1024},\ \ \ \ P(6\ white+4\ red) = \begin{pmatrix} 10\\6 \end{pmatrix}\times (\frac{1}{2})^6\times (\frac{1}{2})^4 = \frac{210}{1024}\\
P(5\ white+5\ red) &= \begin{pmatrix} 10\\5 \end{pmatrix}\times (\frac{1}{2})^5\times (\frac{1}{2})^5 = \frac{252}{1024}\\ 
\end{aligned}
\end{equation}
$$
Set the result of the first 4 draws as event $A$, which is $(2\ white + 2\ red)$.

The probability of $A$ is:
$$
\begin{equation}
\begin{aligned}
P(A) &= \frac {P(2\ white+ 2\ red)}{P(4\ draws)} \\
	 &= \left (P(0\ white+10\ red) \times 0 
	 + P(1\ white+9\ red) \times 0 \\
	 + P(2\ white+8\ red) \times \begin{pmatrix} 2\\2 \end{pmatrix} \times \begin{pmatrix} 8\\2 \end{pmatrix} 
	 + P(3\ white+7\ red) \times  \begin{pmatrix} 3\\2 \end{pmatrix} \times \begin{pmatrix} 7\\2 \end{pmatrix} \\
	 + P(4\ white+6\ red) \times  \begin{pmatrix} 4\\2 \end{pmatrix} \times \begin{pmatrix} 6\\2 \end{pmatrix} 
	 + P(5\ white+5\ red) \times  \begin{pmatrix} 5\\2 \end{pmatrix} \times \begin{pmatrix} 5\\2 \end{pmatrix} \\
	 + P(6\ white+4\ red) \times  \begin{pmatrix} 6\\2 \end{pmatrix} \times \begin{pmatrix} 4\\2 \end{pmatrix} 
	 + P(7\ white+3\ red) \times  \begin{pmatrix} 7\\2 \end{pmatrix} \times \begin{pmatrix} 3\\2 \end{pmatrix} \\
	 + P(8\ white+2\ red) \times  \begin{pmatrix} 8\\2 \end{pmatrix} \times \begin{pmatrix} 2\\2 \end{pmatrix} 
	 + P(9\ white+1\ red) \times 0 
	 + P(10\ white+0\ red) \times 0 \right ) \times \frac{1}{\begin{pmatrix} 10\\4 \end{pmatrix}} \\
	 &= \left ( \frac{45}{1024} \times 1 \times 28 + \frac{120}{1024} \times 3 \times 21 + \frac{210}{1024} \times 6 \times 15 + \frac{252}{1024} \times 10 \times 10 \\
	 + \frac{210}{1024} \times 15 \times 6 + \frac{120}{1024} \times 21 \times 3 + \frac{45}{1024} \times 28 \times 1 \right ) \times \frac{1}{210} \\
	 &= \frac{1260+7560+18900+25200+18900+7560+1260}{1024 \times 210} \\
	 &= \frac{80640}{215040} \\
	 &= \frac{3}{8} 
\end{aligned}
\end{equation}
$$








Event $A$ has already happened, so we should refresh the probabilities of the combinations in the box with conditional probability.
$$
\begin{equation}
\begin{aligned}
P(0\ white+10\ red \mid A) 
	&= \frac {P(0\ white+10\ red \cap A)}{P(A)}
	= 0\\
P(1\ white+9\ red \mid A)  
	&= \frac {P(1\ white+9\ red \cap A)}{P(A)}\ \ 
	= 0\\
P(2\ white+8\ red \mid A)  
	&= \frac {P(2\ white+8\ red \cap A)}{P(A)}\ \ 
	= \frac{P(2\ white+8\ red) \times \begin{pmatrix} 2\\2 \end{pmatrix} \times \begin{pmatrix} 8\\2 \end{pmatrix} \times \frac{1}{\begin{pmatrix} 10\\4 \end{pmatrix}}}{\frac{3}{8} } \\
	&= \ \  \frac{\frac{45}{1024} \times 1 \times 28 \times \frac{1}{210}}{\frac{3}{8} }
	= \ \ \ \ \frac{45 \times 1 \times 28 \times 1 \times 8}{1024 \times 210 \times 3} 
	= \frac{1}{64} \\
P(3\ white+7\ red \mid A)  
	&= \frac {P(3\ white+7\ red \cap A)}{P(A)}\ \ 
	= \frac{P(3\ white+7\ red) \times  \begin{pmatrix} 3\\2 \end{pmatrix} \times \begin{pmatrix} 7\\2 \end{pmatrix}\times \frac{1}{\begin{pmatrix} 10\\4 \end{pmatrix}}}{\frac{3}{8} } \\
	&= \ \  \frac{\frac{120}{1024} \times 3 \times 21\times \frac{1}{210}}{\frac{3}{8} }
	= \ \ \frac{120 \times 3 \times 21 \times 1 \times 8}{1024 \times 210 \times 3} 
	= \frac{6}{64} \\
P(4\ white+6\ red \mid A)  
	&= \frac {P(4\ white+6\ red \cap A)}{P(A)}\ \ 
	= \frac{P(4\ white+6\ red) \times  \begin{pmatrix} 4\\2 \end{pmatrix} \times \begin{pmatrix} 6\\2 \end{pmatrix}\times \frac{1}{\begin{pmatrix} 10\\4 \end{pmatrix}}}{\frac{3}{8} } \\
	&= \ \ \frac{\frac{210}{1024} \times 6 \times 15\times \frac{1}{210}}{\frac{3}{8} }
	= \ \ \frac{210 \times 6 \times 15 \times 1 \times 8}{1024 \times 210 \times 3} 
	= \frac{15}{64} \\
P(5\ white+5\ red \mid A)  
	&= \frac {P(5\ white+5\ red \cap A)}{P(A)}\ \ 
	= \frac{P(5\ white+5\ red) \times  \begin{pmatrix} 5\\2 \end{pmatrix} \times \begin{pmatrix} 5\\2 \end{pmatrix}\times \frac{1}{\begin{pmatrix} 10\\4 \end{pmatrix}}}{\frac{3}{8} } \\
	&= \frac{\frac{252}{1024} \times 10 \times 10\times \frac{1}{210}}{\frac{3}{8} }
	= \frac{252 \times 10 \times 10 \times 1 \times 8}{1024 \times 210 \times 3} 
	= \frac{20}{64} \\
P(6\ white+4\ red \mid A)  
	&= \frac {P(6\ white+4\ red \cap A)}{P(A)}\ \ 
	= \frac{P(6\ white+4\ red) \times  \begin{pmatrix} 6\\2 \end{pmatrix} \times \begin{pmatrix} 4\\2 \end{pmatrix}\times \frac{1}{\begin{pmatrix} 10\\4 \end{pmatrix}}}{\frac{3}{8} } \\
	&= \ \ \frac{\frac{210}{1024} \times 15 \times 6\times \frac{1}{210}}{\frac{3}{8} }
	= \ \ \frac{210 \times 15 \times 6 \times 1 \times 8}{1024 \times 210 \times 3} 
	= \frac{15}{64} \\
P(7\ white+3\ red \mid A)  
	&= \frac {P(7\ white+3\ red \cap A)}{P(A)}\ \ 
	= \frac{P(7\ white+3\ red) \times  \begin{pmatrix} 7\\2 \end{pmatrix} \times \begin{pmatrix} 3\\2 \end{pmatrix}\times \frac{1}{\begin{pmatrix} 10\\4 \end{pmatrix}}}{\frac{3}{8} } \\
	&= \ \ \frac{\frac{120}{1024} \times 21 \times 3\times \frac{1}{210}}{\frac{3}{8} }
	= \ \ \frac{120 \times 21 \times 3 \times 1 \times 8}{1024 \times 210 \times 3} 
	= \frac{6}{64} \\
P(8\ white+2\ red \mid A)  
	&= \frac {P(8\ white+2\ red \cap A)}{P(A)}\ \ 
	= \frac{P(8\ white+2\ red) \times  \begin{pmatrix} 8\\2 \end{pmatrix} \times \begin{pmatrix} 2\\2 \end{pmatrix}\times \frac{1}{\begin{pmatrix} 10\\4 \end{pmatrix}}}{\frac{3}{8} } \\
	&= \ \ \frac{\frac{45}{1024} \times 28 \times 1\times \frac{1}{210}}{\frac{3}{8} }
	= \ \ \ \ \frac{45 \times 28 \times 1 \times 1 \times 8}{1024 \times 210 \times 3} 
	= \frac{1}{64} \\
P(9\ white+1\ red \mid A)  
	&= \frac {P(9\ white+1\ red \cap A)}{P(A)}\ \ 
	= 0\\
P(10\ white+0\ red \mid A)  
	&= \frac {P(10\ white+0\ red \cap A)}{P(A)}
	= 0\\
\end{aligned}
\end{equation}
$$
























Set the difference between white balls and red balls in the result of the next 4 draws as $B$.

Because of putting 4 balls back after the first round, event $A$ and event $B$ are $Statistical\ Independent$.

Below is the conditional probability of the difference between the number of red and white balls drawn in the second round given event $A$：
$$
\begin{equation}
\begin{aligned}
P(\left|B\right|=10 \mid A) 
	&= \frac {P(B=10 \cap A)}{P(A)} 
	= P(\left|B\right|=10) 
	= P(0\ white+10\ red \mid A) 
	= 0 \\
P(\left|B\right|=8  \mid A) \ \ 
    &= \frac {P(B=8  \cap A)}{P(A)}\ \ 
    = P(\left|B\right|=8) \ \ 
	= P(1\ white+9\ red \mid A) + P(9\ white+1\ red \mid A) 
    = 0 \\
P(\left|B\right|=6  \mid A) \ \ 
    &= \frac {P(B=6  \cap A)}{P(A)} \ \ 
    = P(\left|B\right|=6) \ \ 
    = P(2\ white+8\ red \mid A) + P(8\ white+2\ red \mid A) 
    = \frac{1}{64} + \frac{1}{64} 
    = \frac{1}{32} \\
P(\left|B\right|=4  \mid A) \ \ 
    &= \frac {P(B=4  \cap A)}{P(A)} \ \ 
    = P(\left|B\right|=4) \ \ 
    = P(3\ white+7\ red \mid A) + P(7\ white+3\ red \mid A) 
    = \frac{6}{64} + \frac{6}{64} 
    = \frac{6}{32}\\
P(\left|B\right|=2  \mid A) \ \ 
    &= \frac {P(B=2  \cap A)}{P(A)} \ \ 
    = P(\left|B\right|=2) \ \ 
    = P(4\ white+6\ red \mid A) + P(6\ white+4\ red \mid A) 
    = \frac{15}{64} + \frac{15}{64} 
    = \frac{15}{32}\\
P(\left|B\right|=0  \mid A) \ \ 
    &= \frac {P(B=0  \cap A)}{P(A)} \ \ 
    = P(\left|B\right|=0) \ \ 
    = P(6\ white+6\ red \mid A)
    = \frac{10}{32}
\end{aligned}
\end{equation}
$$


Expected value:
$$
\begin{equation}
\begin{aligned}
E(\left|Number_{white} - Number_{red}  \right|) 
	&= E(\left| B \right|) \\ 
	&= 
	10 \times P(\left|B\right|=10 \mid A) \\
	&\ \ \ \ + 8 \times P(\left|B\right|=8 \mid A) \\
	&\ \ \ \ + 6 \times P(\left|B\right|=6 \mid A) \\
	&\ \ \ \ + 4 \times P(\left|B\right|=4 \mid A) \\
	&\ \ \ \ + 2 \times P(\left|B\right|=2 \mid A) \\
	&\ \ \ \ + 0 \times P(\left|B\right|=0 \mid A) \\
    &=  10 \times 0
       +  8 \times 0
       +  6 \times \frac{1}{32}
       +  4 \times \frac{6}{32}
       +  2 \times \frac{15}{32}
       +  0 \times \frac{10}{32} \\
    &= \frac{6 + 24 + 30}{32} \\
    &= 2
\end{aligned}
\end{equation}
$$












