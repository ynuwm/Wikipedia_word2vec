## Wikipedia Data：
### 英文：https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2
### 中文：https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2
### wiki_xml_to_text.py 将维基里的每篇文章转换位1行text文本，并且去掉了标点符号等内容
### Usage： python process_wiki.py enwiki-latest-pages-articles.xml.bz2 wiki.en.text

### train_w2v_model.py 训练word2vector模型，输出为gensim中默认格式的word2vec model和原始c版本word2vec的vector格式的模型: wiki.en.text.vector
### Usage： python train_w2v_model.py wiki.en.text wiki.en.text.model wiki.en.text.vector
