#dictionary는 순서가 없는 집합이다.
#immutable한 키(key)와 mutable한 값(value)으로 맵핑되어있다
#키(key)로 쓰일 수 있는 객체 : int, tuple, float, bool
#키(key))으로 쓰일 수 있는 객체 : set, list, dict
# 순서가 없기 때문에 index로는 접근할 수 없고, 키로 접근할 수 있다 
d = {"a":{1},"b":2}
print(d)
print(d["a"])