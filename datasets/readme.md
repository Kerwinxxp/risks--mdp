Datasets (source):
- db_ACSEmployement: This dataset is generated from the Folktables Python package (https://github.com/zykls/folktables) that provides access to datasets derived from the US Census. We have selected the "Montana" state only, which results in n=10336 samples with d=18 discrete attributes (target included) and domain size **k**=[92, 25, 5, 2, 2, 9, 4, 5, 5, 4, 2, 18, 2, 2, 3, 9, 3, 6].
- db_Adult: This is a classical dataset from the UCI ML repository (https://archive.ics.uci.edu/ml/datasets/adult) with n=45222 samples after cleaning. We selected d=10 attributes ("age",	"workclass", "education",	"marital-status", "occupation", "relationship", "race", "sex", "native-country" and "salary") with domain size **k**=[74, 7, 16, 7, 14, 6, 5, 2, 41, 2], respectively.  


数据集（来源）：
- db_ACSEmployement：该数据集由Folktables Python包（https://github.com/zykls/folktables）生成，该包提供了从美国人口普查数据派生的数据集。我们选择了“蒙大拿”州的数据，包含n=10336个样本，d=18个离散属性（包括目标属性），域大小**k**=[92, 25, 5, 2, 2, 9, 4, 5, 5, 4, 2, 18, 2, 2, 3, 9, 3, 6]。
- db_Adult：这是来自UCI ML库的经典数据集（https://archive.ics.uci.edu/ml/datasets/adult），清洗后包含n=45222个样本。我们选择了d=10个属性（“年龄”、“工作类别”、“教育程度”、“婚姻状况”、“职业”、“关系”、“种族”、“性别”、“本国”、“薪水”），其域大小分别为**k**=[74, 7, 16, 7, 14, 6, 5, 2, 41, 2]。