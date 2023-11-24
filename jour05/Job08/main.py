def my_sort(arr):
    # Initialiser le nombre total de coups à zéro
    total_coups = 0
    
    # Utiliser un indicateur pour savoir si des échanges ont été effectués pendant la passe actuelle
    echanges_effectues = True
    
    # Tant qu'il y a eu des échanges pendant la dernière passe
    while echanges_effectues:
        # Réinitialiser l'indicateur des échanges pour cette nouvelle passe
        echanges_effectues = False
        
        # Parcourir la liste jusqu'à l'avant-dernier élément
        for i in range(len(arr) - 1):
            # Comparer les éléments adjacents et les échanger si nécessaire
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                # Incrémenter le nombre total de coups
                total_coups += 1
                # Mettre à jour l'indicateur des échanges
                echanges_effectues = True
    
    # Afficher le nombre total de coups nécessaires et la liste triée
    print("Nombre total de coups nécessaires pour trier la liste :", total_coups)
    print("Liste triée :", arr)

# Exemple d'utilisation
ma_liste = [34, 25, 12, 22, 11, 64, 90]
my_sort(ma_liste)
