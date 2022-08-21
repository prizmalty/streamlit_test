import imp
from random import sample
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

# プログレスバーの表示
st.write("プログレスバーの表示")
"Start!"
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i+1)
    time.sleep(0.01)

"Done!"

st.title("Streamlit・超入門")
st.write("DataFrame")

df = pd.DataFrame(
    {
        "1列目":[1,2,3,4],
        "2列目":[10,20,30,40]
    }
)
#上で定義したpandas dataframeが表せる
#st.write(df)

#st.dataframeで、writeにはない引数が使える
#st.dataframe(df,width = 100,height =100)

#例
#st.dataframe(df.style.highlight_max(axis=0))

#静的なテーブルを作るときはこう
st.table(df.style.highlight_max(axis=0))

#markdownを書くことも出来る
"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

df_2 = pd.DataFrame(
        np.random.rand(20,3),
        columns=["a","b","c"]
)

#静的なテーブルを作るときはこう
st.table(df_2.style.highlight_max(axis=0))
#折れ線グラフ
st.line_chart(df_2)
#エリアチャート
st.area_chart(df_2)
#棒グラフ
st.bar_chart(df_2)

#新宿区付近の緯度経度でマッピングする
df_3 = pd.DataFrame(
        np.random.rand(100,2)/[50,50]+[35.69,139.70],
        columns=["lat","lon"]
)
#st.mapの引数が緯度経度
st.map(df_3)

#画像を表示
sample_image = Image.open("Amazon.co.jp_ 高地戦（字幕版）を観る _ Prime Video (1).png")
st.image(sample_image,caption = "かわいい",use_column_width = True)

#インタラクティブな機能
st.write("Interactive widgets")
#チェックボックス
if st.checkbox("show Image"):
    sample_image = Image.open("Amazon.co.jp_ 高地戦（字幕版）を観る _ Prime Video (1).png")
    st.image(sample_image)

#選択   
option = st.selectbox(
    "あなたが好きな数字を教えて下さい",
    list(range(1,11))
)
"あなたが好きな数字は、", option,"です。"

#テキスト入力
text = st.text_input("あなたの趣味を教えて下さい")
"あなたの趣味:",text

#スライダー
condition = st.slider("あなたの今の調子は？",0,100,50)
"コンディション:", condition

#サイドバー表示
#テキスト入力
#text_2 = st.sidebar.text_input("あなたの趣味を教えて下さい")
#"あなたの趣味:",text_2

#スライダー
#condition_2 = st.sidebar.slider("あなたの今の調子は？",0,100,50)
#"コンディション:", condition_2

#ボタン
#left_column,right_column = st.beta_columns(2)　betaは書かない
left_column,right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("気持ちええ！")

#expander
expander1 = st.expander("問い合わせ1")
expander1.write("うるせえ！")
expander2 = st.expander("問い合わせ2")
expander2.write("自分でググれ！")

