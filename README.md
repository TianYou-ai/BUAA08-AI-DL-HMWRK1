# BUAA08-AI-DL-HMWRK1
# 人工智能与深度学习小组作业1
动物识别系统
一、目的实现基于产生式规则的专家系统，需要体现专家系统的基本结构。
二、使用python语言实现系统，构造规则库和综合数据库（关系数据库、Excel或TXT皆可），并能对规则库和数据库进行增加、删除和修改操作。
三、简单动物识别系统可以识别多种动物，如：老虎、金钱豹、斑马、长颈鹿、企鹅、鸵鸟、信天翁。建立识别N种动物识别系统的规则：
由于实验要求系统的规则库和综合数据库能够进行增加、删除和修改操作，因此可以采取逐步添加条件，压缩范围的方法进行识别，即：
先跟据一些动物的共性进行大致分类，然后在添加约束条件，将范围缩小，直到能够识别出每一种不同的动物为止。这样，我们在需要添加识别其他动物的功能时，只需要添加那些动物的个性方面的信息即可，这样也可以简化系统的结构和内容。识别老虎、金钱豹、斑马、长颈鹿、企鹅、鸵鸟、信天翁等多种动物的简单动物识别系统基础规则有以下15条：
Rule1 IF 该动物有毛发 THEN 该动物是哺乳动物
Rule2 IF 该动物有奶 THEN 该动物是哺乳动物
Rule3 IF该动物有羽毛 THEN 该动物是鸟
Rule4 IF 该动物会飞 AND会下蛋  THEN 该动物是鸟
Rule5 IF 该动物吃肉 THEN 该动物是肉食动物 
Rule6 IF 该动物有犬齿AND有爪 AND眼盯前方THEN该动物是肉食动物
Rule7 IF 该动物是哺乳动物 AND 有蹄 THEN 该动物是有蹄类动物
Rule8 IF 该动物是哺乳动物 AND 是嚼反刍动物 THEN 该动物是有蹄类动物
Rule9 IF 该动物是哺乳动物 AND 是肉食动物 AND 是黄褐色AND 身上有暗斑点THEN该动物是金钱豹
Rule10 IF 该动物是哺乳动物 AND 是肉食动物 AND 是黄褐色AND 身上有黑色条纹 THEN 该动物是老虎
Rule11 IF 该动物是有蹄类动物 AND 有长脖子 AND 有长腿 AND 身上有暗斑点 THEN 该动物是有长颈鹿
Rule12 IF 该动物是有蹄类动物 AND 身上有黑色条纹 THEN 该动物是斑马 
Rule13 IF 该动物是鸟 AND 有长脖子 AND 有长腿 AND不会飞 THEN 该动物是鸵鸟  
Rule14 IF 该动物是鸟 AND 会游泳 AND 有黑白二色 AND不会飞 THEN 该动物是企鹅  
Rule15 IF 该动物是鸟 AND 善飞 THEN 该动物是信天翁
