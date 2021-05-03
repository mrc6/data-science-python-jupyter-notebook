import sys
import pandas as pd
import numpy as np
import pandas_profiling
import re

#Exemplos de uso do pandas
def mainLoop():
    print('Bem vindo ao mundo da análise de dados')
    #df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
    #print(df.head())
    #print(df.info())
    #df.set_index('PassengerId', inplace=True)
    #print(df.head())
    #print(df.columns)
    #print(df.loc[1])
    #print(df.loc[[1,2,3]])
    #print(df.loc[10:30:2])
    #print(df[['Name','Sex','Age']])
    #print(df.loc[1:10,['Name','Sex','Age']])
    #print(df.query('Age > 20').head())
    #print(df.query('Age > 20 & Sex=="male"').head(10))
    #print(df.query('Age > 20 | Sex=="male"').head(10))
    #print(df.select_dtypes(include='object'))
    #print(df.select_dtypes(include='float'))
    ## gerar um relatório overview sobre a base de dados
    #Profile=pandas_profiling.ProfileReport(df)
    #Profile.to_widgets() #gera no jupyter
    #Profile.to_file('report.html') #salva o arquivo
    # fim gerar um relatorio overview sobre a base de dados
    #print(df.groupby(by='Sex').size())
    #print(df.Sex.value_counts())
    #print(df.groupby(by='Sex')['Age'].mean())
    ## manipulando como séries
    #sl1=df.groupby(by='Sex')['Age'].mean()
    #print(sl1.index.values.tolist())
    #print(sl1.values.tolist())
    ## fim do manipulando com séries
    #print(df.groupby(['Sex','Survived']).agg({'Age': np.mean, 'PassengerId': np.size}))
    #print(df.sample(n=50).head())
    #print(df.sample(frac=.25, random_state=1).head())
    ## dados faltantes
    #print(df.isnull().sum())
    ## preencher valores faltantes
    #print(df.fillna(0))
    #print(df.fillna(df.Age.mean()))
    #print(df.fillna(method='ffill'))
    #print(df.fillna(method='bfill'))
    #values = {'Age': df.Age.mode()[0], 'Cabin': 'SC', 'Embarked': df.Embarked.mode()[0]}
    #df.fillna(value=values, inplace=True)
    #print(df.head())
    #print(df.isnull().sum())
    ## fim do preencher valores faltantes
    ## trabalhando com strings
    #print(df.Name.str.rstrip().head())
    #print(df.Name.str.strip().head())
    #print(df.Name.str.lower().head())
    #print(df.Name.str.upper().head())
    #def remove_parenteses(item):
    #    if '(' in item:
    #        return item.replace('(','').replace(')','')
    #    else:
    #        return item
    #print(df.Name.head().apply(remove_parenteses))
    #print(df.loc[df.Name.str.contains('Mr', flags=re.I, regex=True)].head())
    #def checa_nome(name, last_letter):
    #    if re.search('Mr', name):
    #        return last_letter
    #    else:
    #        return 0
    #df['Mr_name'] = df.Name.apply(lambda x: checa_nome(x, x[-1]))
    #print(df.head(20))
    ## fim do trabalhando com strings
    ## lendo bases grandes
    #df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv', sep=',', nrows=5)
    #print(df.columns.tolist())
    #print(df)
    #data = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
    #df = pd.read_csv(data, usecols=lambda column: column not in ['Parch', 'Ticket', 'Fare', 'Cabin'])
    #print(df.head(10))
    #print(df.info())
    ## Convertendo os tipos de dados
    ## exemplo 1
    #df = pd.read_csv(data)
    
    #print(df.info())
    
    #df.Sex = df.Sex.astype('category')
    #df.Embarked = df.Embarked.astype('category')
    #df.Survived = df.Survived.astype('category')
    #df.Pclass = df.Pclass.astype('category')
    #df.PassengerId = df.PassengerId.astype('int32')
    #df.Parch = df.Parch.astype('int32')
    #df.SibSp = df.SibSp.astype('int32')
    
    #print(df.info())
    ## fim do exemplo 1
    ## exemplo 2
    #df = pd.read_csv(data)
    #print(df.info())
    
    #df = pd.read_csv(data, dtype={
    #    'Sex': 'category',
    #    'Embarked':'category',
    #    'Survived': 'category',
    #    'Pclass': 'category',
    #    'PassengerId': 'int32',
    #    'Parch': 'int32',
    #    'SibSp': 'int32'
    #})
    #print(df.info())
    ## fim do exemplo 2
    ## dividindo a base de dados
    ## exemplo 1
    #df = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    #for d in pd.read_csv(df, chunksize=200):
    #    print ("Chunk")
    #    print(d.count())
    ## fim do exemplo 1
    ## exemplo 2
    age_mean = []
    age_std = []
    sex_dist = []
    male_count = []
    female_count = []

    for d in pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv", chunksize=200):
        age_mean.append(d.Age.mean())
        age_std.append(d.Age.std())
        male_count.append(d.Sex.value_counts().values[0])
        female_count.append(d.Sex.value_counts().values[1])

    print (age_mean)
    print (age_std)
    print (male_count)
    print (female_count)
    ## fim do exemplo 2
    ## fim do dividindo a base de dados
    ## fim do lendo bases grandes
    
if __name__ == '__main__':
    mainLoop()