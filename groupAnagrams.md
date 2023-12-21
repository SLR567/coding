# 字母异位词分组

给你一个字符串数组，请你将***字母异位词***组合在一起。可以按任意顺序返回结果列表。

***字母异位词***是由重新排列源单词的所有字母得到的一个新单词。

***示例 1:***
输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]

***示例 2:***
输入: strs = [""]
输出: [[""]]

***示例 3:***
输入: strs = ["a"]
输出: [["a"]]

***解答：***


```python
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = []
        dic = {}
        for s in strs:
            keys="".join(sorted(s))
            if keys not in dic:
                dic[keys]=[s]
            else:
                dic[keys].append(s)
        return list(dic.values())
```
