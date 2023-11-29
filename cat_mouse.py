def cat_mouse(map, moves):
    '''Функция выясняет, сможет ли кошка поймать мышь из текущего положения,
    Если одно из двух животных отсутствует, вернитесь "boring without two animals".
    '''
    if 'C' not in map or 'm' not in map:
        return "boring without two animals"
    
    map_rows = map.split()

    for index_row, row in enumerate(map_rows):
        if 'm' in row:
            index_m_col = row.index('m')
            index_m_str = index_row
        if 'C' in row:
            index_c_col = row.index('C')
            index_c_str = index_row
    
    distance = abs((index_m_col + index_m_str) - (index_c_col + index_c_str))

    return "Caught!" if distance <= moves else "Escaped!"
