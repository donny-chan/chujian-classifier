import argparse
import os


def get_parser():
    p = argparse.ArgumentParser()
    p.add_argument(
        '--data_dir',
        default='./data/8')
    p.add_argument(
        '-exp', '--ckpt_dir',
        type=str,
        help='root where to store models, losses and accuracies',
        default='./ckpts')
    # 改了，原100
    p.add_argument(
        '-nep', '--epochs',
        type=int,
        help='number of epochs to train for',
        default=1)
    p.add_argument(
        '-lr', '--learning_rate',
        type=float,
        help='learning rate for the model, default=0.001',
        default=0.001)
    # 学习率衰减用的
    p.add_argument('-lrS', '--lr_scheduler_step',
                        type=int,
                        help='StepLR learning rate scheduler step, default=20',
                        default=20)

    p.add_argument('-lrG', '--lr_scheduler_gamma',
                        type=float,
                        help='StepLR learning rate scheduler gamma, default=0.5',
                        default=0.5)
    # 改了，原100
    p.add_argument('-its', '--iterations',
                        type=int,
                        help='number of episodes per epoch, default=100',
                        default=100)

    p.add_argument('-cTr', '--classes_per_it_tr',
                        type=int,
                        help='number of random classes per episode for training, default=60',
                        default=60)

    p.add_argument('-nsTr', '--num_support_tr',
                        type=int,
                        help='number of samples per class to use as support for training, default=5',
                        default=5)

    p.add_argument('-nqTr', '--num_query_tr',
                        type=int,
                        help='number of samples per class to use as query for training, default=5',
                        default=5)

    p.add_argument('-cVa', '--classes_per_it_val',
                        type=int,
                        help='number of random classes per episode for validation, default=5',
                        default=5)
    # 改了，原5
    p.add_argument('-nsVa', '--num_support_val',
                        type=int,
                        help='number of samples per class to use as support for validation, default=5',
                        default=4)
    # 改了，原15
    p.add_argument('-nqVa', '--num_query_val',
                        type=int,
                        help='number of samples per class to use as query for validation, default=15',
                        default=4)
    # 用来搞随机数
    p.add_argument(
        '--seed', type=int, default=0,
        help='input for the manual seeds initializations',)

    p.add_argument(
        '--cuda', type=bool, default=True,
        help='enables cuda',)

    return p
