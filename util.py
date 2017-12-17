# 配列からindexに該当する数値を取り出すが, indexが範囲外ならdefaultを返す
def safe_array_get (array, index, default):
    if array is None:
        return default

    try:
        return array[index]
    except IndexError:
        return default
