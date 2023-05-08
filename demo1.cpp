#include<stdio.h>
#include<string.h>

enum kind{
/*无定义,标识符,整数,void,int,float*/UNDEFINED,SYMBOL,INTEGER,VOID,INT,FLOAT, \
/*char,if,else,while,do,for,return*/CHAR,IF,ELSE,WHILE,DO,FOR,RETURN, \
/*main,+,-,*,/,%*/MAIN,ADD,SUB,MUL,DIV,MOD, \
/*<,<=,>,>=,==,!=*/LT,LET,GT,GET,EQUAL,NEQUAL, \
/*&&,||,,=*/AND,OR,ASSIGNMENT, \
/*(,),[,],{,}*/LEFTPAR,RIGHTPAR,LEFTBUCKET,RIGHTBUCKET,OPENBRACE,CLOSEBRACE, \
/*;,,error*/SEMICOLON,COMMAN,ERROR};

struct word
{
	char *name;
	enum kind id;
};

#define MAX_WORD 1000
#define MAX_CHAR 25

struct word judge_symbol(char *s,int n);

int length[MAX_WORD] ={0};

int main()
{
	char symbol = 0;
	char s[MAX_WORD][MAX_CHAR]={0};
	int num = 1;
	int i = 0,j = 0;
	bool requset_next = 0,put_here = 0,E_flag = 0;
	int comment_flag = 0;
	bool comment_flag2 = 0;
	
	while((symbol = getchar()) != '#' )
	{
		if(symbol != '=')E_flag=0;
		
		//判断注释 
		if(comment_flag == 1)
		{
			if(symbol != '/' && symbol != '*')comment_flag = 0;
			if(symbol == '*')
			{
				comment_flag2 = 1;
				comment_flag = 0;
				length[i]--;
				s[i][j-1] = 0;
				j--;
				continue;
			}
			if(symbol == '/' && comment_flag2)
			{
				comment_flag2 = 0;
				comment_flag = 0;
				continue;
			}
		}
		else if(comment_flag == 2)
		{
			if(symbol != '\n')
			{
				continue;
			}
			else 
			{
				length[i]-=2;
				s[i][j-1] = 0;
				s[i][j-2] = 0;
				j-=2;
				comment_flag = 0;
			}
		}
		if(comment_flag2)
		{
			if(symbol != '*' && symbol != '/')continue;
			if(symbol == '*')
				{
					comment_flag++;
					continue;
				}
		}
		
		
		if(symbol == '\n')
		{
			if(j!=0&&s[i][0]!='\n')
			{
				num++;
				if(!put_here)
				{
					i++;
					j = 0;
				}
				requset_next = 1;
			}
			else continue;
		}
		else if(symbol == '\t')
		{
			continue;
		}
		else if(symbol == ' ')
		{
			if(!requset_next)
			{
				i++;
				j = 0;
				put_here = 1;
			}
			continue;
		}
		else if(symbol == '[' || symbol == ']')
		{
			if(!put_here)
			{
				i++;
				j = 0;
			}
			requset_next = 1;
		}
		else if(symbol == '{' || symbol == '}')
		{
			if(!put_here)
			{
				i++;
				j = 0;
			}
			requset_next = 1;
		}
		else if(symbol == '(' || symbol == ')')
		{
			if(!put_here)
			{
				i++;
				j = 0;
			}
			requset_next = 1;
		}
		else if(symbol == ';'||symbol == ',')
		{
			if(!put_here)
			{
				i++;
				j = 0;
			}
			requset_next = 1;
		}
		else if(symbol == '=')
		{
			if(!put_here && !E_flag)
			{
				i++;
				j = 0;
			}
			if(E_flag)E_flag = 0;
			else 
			{
				E_flag = 1;
			}
			requset_next = 1;
		}
		else if(symbol == '>' || symbol == '<')
		{
			if(!put_here)
			{
				i++;
				j = 0;
			}
			requset_next = 1;
			E_flag = 1;
		}
		else if(symbol == '!')
		{
			if(!put_here)
			{
				i++;
				j = 0;
			}
			requset_next = 1;
			E_flag = 1;
		}
		else if(symbol == '+' || symbol == '-')
		{
			if(!put_here)
			{
				i++;
				j = 0;
			}
			requset_next = 1;
		}
		else if(symbol == '*')
		{
			if(!put_here)
			{
				i++;
				j = 0;
			}
			requset_next = 1;
		}
		else if(symbol == '/')
		{
			if(!put_here && !comment_flag)
			{
				i++;
				j = 0;
			}
			requset_next = 1;
			comment_flag++;
		}
		else
		{
			put_here = 0;
			if(requset_next)
			{
				i++;
				j = 0;
				requset_next = 0;
			}
		}
		s[i][j++] = symbol;
		length[i]++;
	}
	i++;
	struct word S;
	int lines = 1;
	int error_lines[num] = {0};
	int error_num = 0;
	for (int x = 0;x<i;x++)
	{
		if(s[x][0] != '\n' && length[x])
		{
			S = judge_symbol(s[x],x);
			if(S.id == ERROR)
			{
				printf("LexicalError,");
				error_lines[error_num] = lines;
				error_num++;
			}
			else printf("<%d,%s>,",S.id,S.name);
		}
		else
			{
				printf("\n");
				lines++;
			}
	}
	if(error_num)
	{
		printf("LexicalError(s) on line(s) ");
		for(int temp = 0;temp < error_num;temp++)
		{
			printf("%d,",error_lines[temp]);
		}
	}
	return 0;
}

struct word judge_symbol(char *s,int n)
{
	struct word S;
	S.name = "-";
	if(!strcmp(s,"void"))
	{
		S.id = VOID;
	}
	else if(!strcmp(s,"int"))
	{
		S.id = INT;
	}
	else if(!strcmp(s,"float"))
	{
		S.id = FLOAT;
	}
	else if(!strcmp(s,"char"))
	{
		S.id = CHAR;
	}
	else if(!strcmp(s,"if"))
	{
		S.id = IF;
	}
	else if(!strcmp(s,"else"))
	{
		S.id = ELSE;
	}
	else if(!strcmp(s,"while"))
	{
		S.id = WHILE;
	}
	else if(!strcmp(s,"do"))
	{
		S.id = DO;
	}
	else if(!strcmp(s,"for"))
	{
		S.id = FOR;
	}
	else if(!strcmp(s,"return"))
	{
		S.id = RETURN;
	}
	else if(!strcmp(s,"main"))
	{
		S.id = MAIN;
	}
	else if(!strcmp(s,"+"))
	{
		S.id = ADD;
	}
	else if(!strcmp(s,"-"))
	{
		S.id = SUB;
	}
	else if(!strcmp(s,"*"))
	{
		S.id = MUL;
	}
	else if(!strcmp(s,"/"))
	{
		S.id = DIV;
	}
	else if(!strcmp(s,"%"))
	{
		S.id = MOD;
	}
	else if(!strcmp(s,"<"))
	{
		S.id = LT;
	}
	else if(!strcmp(s,"<="))
	{
		S.id = LET;
	}
	else if(!strcmp(s,">"))
	{
		S.id = GT;
	}
	else if(!strcmp(s,">="))
	{
		S.id = GET;
	}
	else if(!strcmp(s,"=="))
	{
		S.id = EQUAL;
	}
	else if(!strcmp(s,"!="))
	{
		S.id = NEQUAL;
	}
	else if(!strcmp(s,"&&"))
	{
		S.id = AND;
	}
	else if(!strcmp(s,"||"))
	{
		S.id = OR;
	}
	else if(!strcmp(s,"="))
	{
		S.id = ASSIGNMENT;
	}
	else if(!strcmp(s,"("))
	{
		S.id = LEFTPAR;
	}
	else if(!strcmp(s,")"))
	{
		S.id = RIGHTPAR;
	}
	else if(!strcmp(s,"["))
	{
		S.id = LEFTBUCKET;
	}
	else if(!strcmp(s,"]"))
	{
		S.id = RIGHTBUCKET;
	}
	else if(!strcmp(s,"{"))
	{
		S.id = OPENBRACE;
	}
	else if(!strcmp(s,"}"))
	{
		S.id = CLOSEBRACE;
	}
	else if(!strcmp(s,";"))
	{
		S.id = SEMICOLON;
	}
	else if(!strcmp(s,","))
	{
		S.id = COMMAN;
	}
	else
	{
		S.name = s;
		if(s[0] >= '0' && s[0] <= '9')
		{
			int i =length[n];
			while(i--)
			{
				if(s[i] < '0' || s[i] > '9')
				{
					S.id = ERROR;
					return S;
				}
			}
			S.id = INTEGER;
		}
		else
		{
			int i = length[n];
			while(i--)
			{
				if(!((*s <= 'z'&& *s >= 'a')||(*s <= 'Z' && *s >= 'A')||(*s <= '9' && *s >= '0') || *s == '_'))
				{
					S.id = UNDEFINED;
					return S;
				}
				s++;
			}
			S.id = SYMBOL;
		}
	}
	return S;
}

