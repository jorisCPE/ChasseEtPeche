import random

def rotation_tuile(tuile,nom):
    tuile_tournes = [[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],]
    
    for i in range(random.randint(1,12)):
        #rotation dans une liste anexe
        tuile_tournes[0][2] = tuile[3][0]
        tuile_tournes[0][3] = tuile[2][1]
        tuile_tournes[0][4] = tuile[1][1]
        tuile_tournes[0][5] = tuile[0][2]
        
        tuile_tournes[1][1] = tuile[4][1]
        tuile_tournes[1][2] = tuile[3][1]
        tuile_tournes[1][3] = tuile[2][2]
        tuile_tournes[1][4] = tuile[1][2]
        tuile_tournes[1][5] = tuile[0][3]
        
        tuile_tournes[2][1] = tuile[5][1]
        tuile_tournes[2][2] = tuile[4][2]
        tuile_tournes[2][3] = tuile[3][2]
        tuile_tournes[2][4] = tuile[2][3]
        tuile_tournes[2][5] = tuile[1][3]
        tuile_tournes[2][6] = tuile[0][4]
        
        tuile_tournes[3][0] = tuile[6][2]
        tuile_tournes[3][1] = tuile[5][2]
        tuile_tournes[3][2] = tuile[4][3]
        tuile_tournes[3][3] = tuile[3][3]
        tuile_tournes[3][4] = tuile[2][4]
        tuile_tournes[3][5] = tuile[1][4]
        tuile_tournes[3][6] = tuile[0][5]
        
        tuile_tournes[4][1] = tuile[6][3]
        tuile_tournes[4][2] = tuile[5][3]
        tuile_tournes[4][3] = tuile[4][4]
        tuile_tournes[4][4] = tuile[3][4]
        tuile_tournes[4][5] = tuile[2][5]
        tuile_tournes[4][6] = tuile[1][5]
        
        tuile_tournes[5][1] = tuile[6][4]
        tuile_tournes[5][2] = tuile[5][4]
        tuile_tournes[5][3] = tuile[4][5]
        tuile_tournes[5][4] = tuile[3][5]
        tuile_tournes[5][5] = tuile[2][6]
        
        tuile_tournes[6][2] = tuile[6][5]
        tuile_tournes[6][3] = tuile[5][5]
        tuile_tournes[6][4] = tuile[4][6]
        tuile_tournes[6][5] = tuile[3][6]
        
        #copie de la liste anexe dans la liste principale
        for j in range(7):
            for k in range(7):
                tuile[j][k] = tuile_tournes[j][k]
    
    return tuile_tournes,nom