import numpy as np
import datetime
import json

N = 10
D = 10
teams = [[0, 0]]  # number of teams
roles = ['CO', 'TW', 'RI', 'IMP', 'PL', 'ME', 'CF', 'SH', 'SP']  # list of roles
minimalNumber = [70, 70, 70, 70, 70, 70, 70, 70, 70]
badRolesInOneEmployeeCombination = [[4, 5], [4, 6], [4, 7], [5, 6], [5, 7], [6, 7]]
goodRolesForDifferentEmployee = [[0, 2], [0, 3],[0,4],[0,5],[0,6],[0,8],[1,2],[1,3],[1,4],[1,5],[1,6],[1,8],[2,5],[3,5],[3,6],[3,7],[3,8],[4,6],[5,8],[6,8]]
badRolesForDifferentEmployee = [[0,1],[0,7],[1,7],[2,3],[2,4],[2,6],[2,7],[2,8],[3,4],[4,5],[4,7],[4,8],[5,6],[5,7],[6,7],[7,8]]


class Map(object):

    def __init__(self, json_data):
        self.badCombinationsOfTwoEmployees = []
        self.employeesWithBadRolesCombinations =[]
        self.employees = []  # persons
        json_data = json.loads(json_data)
        for employee in json_data:
            self.employees.append(employee)
        self.Map = np.zeros((len(roles), len(self.employees), len(teams)))
        for i in range(0, len(self.employees)):
            for j in range(0, len(roles)):
                for t in range(0, len(teams)):
                    if self.employees[i][roles[j]] >= minimalNumber[j]:
                        self.Map[j][i][t] = 1

    def clearMapFromBadRolesinEmployee(self):
        self.employeesWithBadRolesCombinations = []
        for i in range(0, len(self.employees)):
            for j in range(0, len(badRolesInOneEmployeeCombination)):
                for t in range(0, len(teams)):
                    if (self.Map[badRolesInOneEmployeeCombination[j][0]][i][t] == 1 and
                                self.Map[badRolesInOneEmployeeCombination[j][1]][i][t] == 1) or \
                        (self.Map[badRolesInOneEmployeeCombination[j][1]][i][t] == 1 and
                                self.Map[badRolesInOneEmployeeCombination[j][0]][i][t] == 1):

                        if (N - np.absolute(self.employees[i][roles[badRolesInOneEmployeeCombination[j][0]]] - self.employees[i][
                            roles[badRolesInOneEmployeeCombination[j][1]]])) * \
                                self.Map[badRolesInOneEmployeeCombination[j][0]][i][t] > 0:

                            if [badRolesInOneEmployeeCombination[j][0], i] not in self.employeesWithBadRolesCombinations:
                                self.employeesWithBadRolesCombinations.append([badRolesInOneEmployeeCombination[j][0], i])
                            self.Map[badRolesInOneEmployeeCombination[j][0]][i][t] = 0
                            if (N - np.absolute(
                                        self.employees[i][roles[badRolesInOneEmployeeCombination[j][0]]] - self.employees[i][
                                        roles[badRolesInOneEmployeeCombination[j][1]]])) * \
                                    self.Map[badRolesInOneEmployeeCombination[j][1]][i][t] > 0:
                                if [badRolesInOneEmployeeCombination[j][1], i] not in self.employeesWithBadRolesCombinations:
                                    self.employeesWithBadRolesCombinations.append(
                                        [badRolesInOneEmployeeCombination[j][1], i])
                                self.Map[badRolesInOneEmployeeCombination[j][1]][i][t] = 0
        #print(self.Map)

    def compare_emloyees(self, first_employee_team, first_employee, first_employee_role, second_employee_role, second_employee):
        if (np.sign(D - np.absolute(self.employees[first_employee][roles[first_employee_role]] -
                                        self.employees[second_employee][roles[first_employee_role]])) *
                (self.Map[first_employee_role][first_employee][first_employee_team] +
                     self.Map[second_employee_role][second_employee][first_employee_team]) <= 1 and
                        np.sign(D - np.absolute(self.employees[first_employee][roles[second_employee_role]] -
                                                    self.employees[second_employee][roles[second_employee_role]])) *
                        (self.Map[first_employee_role][first_employee][first_employee_team] +
                             self.Map[second_employee_role][second_employee][first_employee_team]) <= 1 and
                        np.sign(self.employees[first_employee][roles[first_employee_role]] -
                                    self.employees[second_employee][roles[first_employee_role]]) *
                        (self.Map[first_employee_role][second_employee][first_employee_team] +
                             self.Map[second_employee_role][first_employee][first_employee_team]) <= 1 and
                        np.sign(self.employees[second_employee][roles[second_employee_role]] -
                                    self.employees[first_employee][roles[second_employee_role]]) *
                        (self.Map[first_employee_role][second_employee][first_employee_team] +
                             self.Map[second_employee_role][first_employee][first_employee_team]) <= 1 and
                        np.sign(self.employees[second_employee][roles[first_employee_role]] -
                                    self.employees[first_employee][roles[first_employee_role]]) *
                        (self.Map[first_employee_role][first_employee][first_employee_team] +
                             self.Map[second_employee_role][second_employee][first_employee_team]) <= 1 and
                        np.sign(self.employees[first_employee][roles[second_employee_role]] -
                                    self.employees[second_employee][roles[second_employee_role]]) *
                        (self.Map[first_employee_role][first_employee][first_employee_team] +
                             self.Map[second_employee_role][second_employee][first_employee_team]) <= 1):
                    return 1
        else:
            return 0

    def suitableEmployeesByRoles(self):
        self.suitableEmployees = []
        for t in range(0, len(teams)):
            for i in range(0, len(self.employees)):
                for j in range(0, len(roles)):
                    if self.Map[j][i][t] == 1:
                        self.suitableEmployees.append([j, i])

        self.resultCO = []
        self.resultTW = []
        self.resultRI = []
        self.resultIMP = []
        self.resultPL = []
        self.resultME = []
        self.resultCF = []
        self.resultSH = []
        self.resultSP = []

        for i in range(0, len(teams)+2):
            self.resultCO.append(-1)
            self.resultTW.append(-1)
            self.resultRI.append(-1)
            self.resultIMP.append(-1)
            self.resultPL.append(-1)
            self.resultME.append(-1)
            self.resultCF.append(-1)
            self.resultSH.append(-1)
            self.resultSP.append(-1)

        for res in self.suitableEmployees:
            if res[0] == 0:
                for i in range(0, len(self.resultCO)):
                    alreadyInList = False
                    for j in self.resultCO:
                        if j == res[1]:
                            alreadyInList = True
                    if self.resultCO[i] != -1:
                        if alreadyInList == False and self.employees[self.resultCO[i]][roles[0]] < self.employees[res[1]][roles[0]]:
                            self.resultCO[i] = res[1]
                    else:
                        if alreadyInList == False:
                            self.resultCO[i] = res[1]

            if res[0] == 1:
                # print("Person ",res[1])
                for i in range(0, len(self.resultTW)):
                    alreadyInList = False
                    for j in self.resultTW:
                        if j == res[1]:
                            alreadyInList = True
                    if self.resultTW[i] != -1:
                        if alreadyInList == False and self.employees[self.resultTW[i]][roles[1]] < self.employees[res[1]][roles[1]]:
                            self.resultTW[i] = res[1]
                    else:
                        if alreadyInList == False:
                            self.resultTW[i] = res[1]
            if res[0] == 2:
                for i in range(0, len(self.resultRI)):
                    alreadyInList = False
                    for j in self.resultRI:
                        if j == res[1]:
                            alreadyInList = True
                    if self.resultRI[i] != -1:
                        if alreadyInList == False and self.employees[self.resultRI[i]][roles[2]] < self.employees[res[1]][roles[2]]:
                            self.resultRI[i] = res[1]
                    else:
                        if alreadyInList == False:
                            self.resultRI[i] = res[1]
            if res[0] == 3:
                for i in range(0, len(self.resultIMP)):
                    alreadyInList = False
                    for j in self.resultIMP:
                        if j == res[1]:
                            alreadyInList = True
                    if self.resultIMP[i] != -1:
                        if alreadyInList == False and self.employees[self.resultIMP[i]][roles[3]] < self.employees[res[1]][roles[3]]:
                            self.resultIMP[i] = res[1]
                    else:
                        if alreadyInList == False:
                            self.resultIMP[i] = res[1]
            if res[0] == 4:
                for i in range(0, len(self.resultPL)):
                    alreadyInList = False
                    for j in self.resultPL:
                        if j == res[1]:
                            alreadyInList = True
                    if self.resultPL[i] != -1:
                        if alreadyInList == False and self.employees[self.resultPL[i]][roles[4]] < self.employees[res[1]][roles[4]]:
                            self.resultPL[i] = res[1]
                    else:
                        if alreadyInList == False:
                            self.resultPL[i] = res[1]

            if res[0] == 5:
                for i in range(0, len(self.resultME)):
                    alreadyInList = False
                    for j in self.resultME:
                        if j == res[1]:
                            alreadyInList = True
                    if self.resultME[i] != -1:
                        if alreadyInList == False and self.employees[self.resultME[i]][roles[5]] < self.employees[res[1]][roles[5]]:
                            self.resultME[i] = res[1]
                    else:
                        if alreadyInList == False:
                            self.resultME[i] = res[1]

            if res[0] == 6:
                for i in range(0, len(self.resultCF)):
                    alreadyInList = False
                    for j in self.resultCF:
                        if j == res[1]:
                            alreadyInList = True
                    if self.resultCF[i] != -1:
                        if alreadyInList == False and self.employees[self.resultCF[i]][roles[6]] < self.employees[res[1]][roles[6]]:
                            self.resultCF[i] = res[1]
                    else:
                        if alreadyInList == False:
                            self.resultCF[i] = res[1]

            if res[0] == 7:
                for i in range(0, len(self.resultSH)):
                    alreadyInList = False
                    for j in self.resultSH:
                        if j == res[1]:
                            alreadyInList = True
                    if self.resultSH[i] != -1:
                        if alreadyInList == False and self.employees[self.resultSH[i]][roles[7]] < self.employees[res[1]][roles[7]]:
                            self.resultSH[i] = res[1]
                    else:
                        if alreadyInList == False:
                            self.resultSH[i] = res[1]

            if res[0] == 8:
                for i in range(0, len(self.resultSP)):
                    alreadyInList = False
                    for j in self.resultSP:
                        if j == res[1]:
                            alreadyInList = True
                    if self.resultSP[i] != -1:
                        if alreadyInList == False and self.employees[self.resultSP[i]][roles[8]] < self.employees[res[1]][roles[8]]:
                            self.resultSP[i] = res[1]
                    else:
                        if alreadyInList == False:
                            self.resultSP[i] = res[1]

        while -1 in self.resultCO:
            self.resultCO.remove(-1)
        while -1 in self.resultTW:
            self.resultTW.remove(-1)
        while -1 in self.resultRI:
            self.resultRI.remove(-1)
        while -1 in self.resultIMP:
            self.resultIMP.remove(-1)
        while -1 in self.resultPL:
            self.resultPL.remove(-1)
        while -1 in self.resultME:
            self.resultME.remove(-1)
        while -1 in self.resultCF:
            self.resultCF.remove(-1)
        while -1 in self.resultSH:
            self.resultSH.remove(-1)
        while -1 in self.resultSP:
            self.resultSP.remove(-1)



    def createTeams(self,CO, TW, RI, IMP, PL, ME, CF, SH, SP):
        team = []
        team.append([0, CO])
        team.append([1, TW])
        team.append([2, RI])
        team.append([3, IMP])
        team.append([4, PL])
        team.append([5, ME])
        team.append([6, CF])
        team.append([7, SH])
        team.append([8, SP])
        Score, team = self.score(team)
        return Score, team

    def score(self, team):

        Score = 0
        deletengEmployees = False
        for i in range(0, len(team)):
            for j in range(0, len(team)):
                if i != j:
                    goodRoleCounter = True

                    for goodRoles in badRolesForDifferentEmployee:
                        if (self.employees[team[i][1]][roles[goodRoles[0]]] >= minimalNumber[goodRoles[0]] and
                                    self.employees[team[j][1]][roles[goodRoles[1]]] >= minimalNumber[goodRoles[1]]) or \
                                (self.employees[team[i][1]][roles[goodRoles[1]]] >= minimalNumber[goodRoles[1]] and
                                         self.employees[team[j][1]][roles[goodRoles[0]]] >= minimalNumber[goodRoles[0]]):

                            goodRoleCounter = False

                    if goodRoleCounter == False and self.employees[team[i][1]]['func_role'] != self.employees[team[j][1]][
                        'func_role']:

                        if self.compare_emloyees(0, team[i][1], team[i][0], team[j][0], team[j][1]) == 0:
                            self.badCombinationsOfTwoEmployees.append(
                                [self.employees[team[i][1]], self.employees[team[j][1]]])
                            deletengEmployees = True
        if deletengEmployees == False:

            for i in team:
                Score += self.employees[i[1]][roles[i[0]]]

        return Score, team

    def finAllPosibleTeams(self):
        self.resultTeam = []
        self.resultTeamScore = 0
        for emloyeeCO in self.resultCO:
            start_time = datetime.datetime.now()
            for emloyeeTW in self.resultTW:

                if emloyeeTW != emloyeeCO:
                    for emloyeeRI in self.resultRI:

                        if emloyeeRI != emloyeeTW and emloyeeRI != emloyeeCO:

                            for emloyeeIMP in self.resultIMP:

                                if emloyeeIMP != emloyeeRI and emloyeeIMP != emloyeeTW and emloyeeIMP != emloyeeCO:
                                    for emloyeePL in self.resultPL:

                                        if emloyeePL != emloyeeIMP and emloyeePL != emloyeeRI and emloyeePL != emloyeeTW and emloyeePL != emloyeeCO:

                                            for emloyeeME in self.resultME:

                                                if emloyeeME != emloyeePL and emloyeeME != emloyeeIMP and emloyeeME != emloyeeRI and emloyeeME != emloyeeTW and emloyeeME != emloyeeCO:
                                                    for emloyeeCF in self.resultCF:

                                                        if emloyeeCF != emloyeeME and emloyeeCF != emloyeePL and emloyeeCF != emloyeeIMP and emloyeeCF != emloyeeRI and emloyeeCF != emloyeeTW and emloyeeCF != emloyeeCO:
                                                            for emloyeeSH in self.resultSH:
                                                                if emloyeeSH != emloyeeME and emloyeeSH != emloyeeCF and emloyeeSH != emloyeePL and emloyeeSH != emloyeeIMP and emloyeeSH != emloyeeRI and emloyeeSH != emloyeeTW and emloyeeSH != emloyeeCO:
                                                                    for emloyeeSP in self.resultSP:
                                                                        if emloyeeSP != emloyeeSH and emloyeeSP != emloyeeME and emloyeeSP != emloyeeCF and emloyeeSP != emloyeePL and emloyeeSP != emloyeeIMP and emloyeeSP != emloyeeRI and emloyeeSP != emloyeeTW and emloyeeSP != emloyeeCO:

                                                                            Score, Team = self.createTeams(emloyeeCO,
                                                                                                      emloyeeTW,
                                                                                                      emloyeeRI,
                                                                                                      emloyeeIMP,
                                                                                                      emloyeePL,
                                                                                                      emloyeeME,
                                                                                                      emloyeeCF,
                                                                                                      emloyeeSH,
                                                                                                      emloyeeSP)

                                                                            if self.resultTeamScore < Score:
                                                                                self.resultTeamScore = Score
                                                                                self.resultTeam = Team

        return self.resultTeamScore,self.resultTeam

    def showEmploeesWithBadRolesCombinations(self):
        return self.employeesWithBadRolesCombinations

    def showBadRoleCombinationsInTwoEmployess(self):
        return self.badCombinationsOfTwoEmployees

def calculations(json_data):
    map = Map(json_data)
    map.clearMapFromBadRolesinEmployee()
    map.suitableEmployeesByRoles()
    resScore, resTeam = map.finAllPosibleTeams()
    return resScore, resTeam, map.showEmploeesWithBadRolesCombinations(), map.showBadRoleCombinationsInTwoEmployess()


