import maya.cmds as cmds

''' 

Fonctionnement :
 1- On selectionne la partie du script jusqu'au group des locator (ligne 40), on execute cette partie
 2- On replace nos locators au besoin
 3- On selectionne le reste du script, et on execute
'''


''' On place des locator dans une position predefinie '''

# Piste d'amelioraton, faire une boucle car repetitif 

Extremite = cmds.spaceLocator(n='Extremite_LOC') # Creation du locator 
cmds.setAttr(Extremite[0] + '.translateX', 7) # Placement du locator 
cmds.setAttr(Extremite[0] + '.translateZ', 8) # Placement du locator 

Orteils = cmds.spaceLocator(n='Orteils_LOC')
cmds.setAttr(Orteils[0] + '.translateX', 7)
cmds.setAttr(Orteils[0] + '.translateY', 0)
cmds.setAttr(Orteils[0] + '.translateZ', 5)

Cheville = cmds.spaceLocator(n='Cheville_LOC')
cmds.setAttr(Cheville[0] + '.translateX', 7)
cmds.setAttr(Cheville[0] + '.translateY', 5)
cmds.setAttr(Cheville[0] + '.translateZ', -2.5)

Genou = cmds.spaceLocator(n='Genou_LOC')
cmds.setAttr(Genou[0] + '.translateX', 7)
cmds.setAttr(Genou[0] + '.translateY', 26)
cmds.setAttr(Genou[0] + '.translateZ', 1)

Hanche = cmds.spaceLocator(n='Hanche_LOC')
cmds.setAttr(Hanche[0] + '.translateX', 7)
cmds.setAttr(Hanche[0] + '.translateY', 46)
cmds.setAttr(Hanche[0] + '.translateZ', 1)

LocGroup = cmds.group(Extremite, Orteils, Cheville, Genou, Hanche, n='LOCATORS') # Grouper les locators


''' On attache un joint a chacun de ces locator '''

ExtremiteJoint = cmds.joint(n='Extremite_Joint') # Creation d'un joint (du meme nom)
constr=cmds.pointConstraint(Extremite, ExtremiteJoint) # Point Constraint pour placer le joint a la meme place que le locator
cmds.delete(constr) # Supprimer la point constraint car plus besoin
cmds.select(d=True) # Deselectionner pour eviter les erreurs

OrteilsJoint = cmds.joint(n='Orteils_Joint')
constr=cmds.pointConstraint(Orteils, OrteilsJoint)
cmds.delete(constr)
cmds.select(d=True)

ChevilleJoint = cmds.joint(n='Cheville_Joint')
constr=cmds.pointConstraint(Cheville, ChevilleJoint)
cmds.delete(constr)
cmds.select(d=True)

GenouJoint = cmds.joint(n='Genou_Joint')
constr=cmds.pointConstraint(Genou, GenouJoint)
cmds.delete(constr)
cmds.select(d=True)

HancheJoint = cmds.joint(n='Hanche_Joint')
constr=cmds.pointConstraint(Hanche, HancheJoint)
cmds.delete(constr)
cmds.select(d=True)


''' Finalement, on parente chaque joint avec le precedent '''

cmds.parent(ExtremiteJoint, OrteilsJoint) # On parente avec le joint au dessus de lui
cmds.parent(OrteilsJoint, ChevilleJoint)
cmds.parent(ChevilleJoint, GenouJoint)
cmds.parent(GenouJoint, HancheJoint)