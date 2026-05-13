#include <stdio.h>

#define MAX_STUDENTS 50   // 最大学生人数
#define COURSE_NUM 3      // 课程数量

// 函数声明
void showMenu(void);
void inputScore(int scores[][COURSE_NUM], int *stuNum);
int calcStuSum(int scores[]);
float calcStuAvg(int sum);
int getCourseMax(int scores[][COURSE_NUM], int stuNum, int courseIdx);
int getCourseMin(int scores[][COURSE_NUM], int stuNum, int courseIdx);
float getCourseAvg(int scores[][COURSE_NUM], int stuNum, int courseIdx);
int countFail(int scores[][COURSE_NUM], int stuNum);
void printAllScore(int scores[][COURSE_NUM], int stuNum);

// 主函数
int main() {
    int scores[MAX_STUDENTS][COURSE_NUM] = {0};  // 存储学生成绩
    int stuNum = 0;                              // 实际学生人数
    int choice;

    showMenu();  // 菜单只显示一次

    do {
        printf("\n请输入功能选择：");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                inputScore(scores, &stuNum);
                break;
            case 2:
                if (stuNum == 0) {
                    printf("请先录入成绩！\n");
                } else {
                    printf("\n========== 个人成绩 ==========\n");
                    printf("学号\t语文\t数学\t英语\t总分\t平均分\n");
                    for (int i = 0; i < stuNum; i++) {
                        int sum = calcStuSum(scores[i]);
                        float avg = calcStuAvg(sum);
                        printf("%d\t%d\t%d\t%d\t%d\t%.2f\n",
                               i + 1, scores[i][0], scores[i][1], scores[i][2], sum, avg);
                    }
                }
                break;
            case 3:
                if (stuNum == 0) {
                    printf("请先录入成绩！\n");
                } else {
                    printf("\n========== 班级各科统计 ==========\n");
                    char *courses[] = {"语文", "数学", "英语"};
                    for (int i = 0; i < COURSE_NUM; i++) {
                        printf("%s - 最高分: %d, 最低分: %d, 平均分: %.2f\n",
                               courses[i],
                               getCourseMax(scores, stuNum, i),
                               getCourseMin(scores, stuNum, i),
                               getCourseAvg(scores, stuNum, i));
                    }
                }
                break;
            case 4:
                if (stuNum == 0) {
                    printf("请先录入成绩！\n");
                } else {
                    int failCount = countFail(scores, stuNum);
                    printf("有不及格科目的学生人数：%d人\n", failCount);
                }
                break;
            case 5:
                if (stuNum == 0) {
                    printf("请先录入成绩！\n");
                } else {
                    printAllScore(scores, stuNum);
                }
                break;
            case 0:
                printf("退出系统\n");
                break;
            default:
                printf("无效选择，请重新输入！\n");
        }
    } while (choice != 0);

    return 0;
}

// 1. 显示菜单（只显示一次）
void showMenu(void) {
    printf("学生成绩统计系统（控制台版）\n");
    printf("1. 录入学生成绩\n");
    printf("2. 输出所有学生成绩明细\n");
    printf("3. 统计班级各科成绩（最高/最低/平均）\n");
    printf("4. 统计有不及格科目的学生人数\n");
    printf("0. 退出系统\n");
}

// 2. 录入成绩
void inputScore(int scores[][COURSE_NUM], int *stuNum) {
    printf("请输入学生总人数（1~%d）：", MAX_STUDENTS);
    scanf("%d", stuNum);

    while (*stuNum < 1 || *stuNum > MAX_STUDENTS) {
        printf("人数无效，请重新输入（1~%d）：", MAX_STUDENTS);
        scanf("%d", stuNum);
    }

    for (int i = 0; i < *stuNum; i++) {
        printf("请输入第 %d 个学生的 语文、数学、英语成绩：", i + 1);
        scanf("%d %d %d", &scores[i][0], &scores[i][1], &scores[i][2]);
    }
    printf("成绩录入完成！\n");
}

// 3. 计算单个学生总分
int calcStuSum(int scores[]) {
    return scores[0] + scores[1] + scores[2];
}

// 4. 计算单个学生平均分
float calcStuAvg(int sum) {
    return sum / (float)COURSE_NUM;
}

// 5. 获取指定课程最高分
int getCourseMax(int scores[][COURSE_NUM], int stuNum, int courseIdx) {
    int max = scores[0][courseIdx];
    for (int i = 1; i < stuNum; i++) {
        if (scores[i][courseIdx] > max) {
            max = scores[i][courseIdx];
        }
    }
    return max;
}

// 6. 获取指定课程最低分
int getCourseMin(int scores[][COURSE_NUM], int stuNum, int courseIdx) {
    int min = scores[0][courseIdx];
    for (int i = 1; i < stuNum; i++) {
        if (scores[i][courseIdx] < min) {
            min = scores[i][courseIdx];
        }
    }
    return min;
}

// 7. 获取指定课程平均分
float getCourseAvg(int scores[][COURSE_NUM], int stuNum, int courseIdx) {
    int sum = 0;
    for (int i = 0; i < stuNum; i++) {
        sum += scores[i][courseIdx];
    }
    return sum / (float)stuNum;
}

// 8. 统计有不及格科目的学生人数
int countFail(int scores[][COURSE_NUM], int stuNum) {
    int failCount = 0;
    for (int i = 0; i < stuNum; i++) {
        for (int j = 0; j < COURSE_NUM; j++) {
            if (scores[i][j] < 60) {
                failCount++;
                break;
            }
        }
    }
    return failCount;
}

// 9. 输出所有学生成绩明细
void printAllScore(int scores[][COURSE_NUM], int stuNum) {
    printf("\n========= 学生成绩明细 ========\n");
    printf("学号\t语文\t数学\t英语\t总分\t平均分\n");
    for (int i = 0; i < stuNum; i++) {
        int sum = calcStuSum(scores[i]);
        float avg = calcStuAvg(sum);
        printf("%d\t%d\t%d\t%d\t%d\t%.2f\n",
               i + 1, scores[i][0], scores[i][1], scores[i][2], sum, avg);
    }
}
