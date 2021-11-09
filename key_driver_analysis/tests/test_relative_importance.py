if __name__ == "__main__":
    import pandas as pd
    from key_driver_analysis import relative_importance

    df = pd.DataFrame(data={
        'age': [40, 50, 60, 10, 20, 30, 7, 80, 90],
        'salary': [123, 4423, 56563, 75545, 2345, 2346, 5534, 775, 34345],
        'no_of_cars_owned': [1, 3, 4, 2, 1, 3, 5, 3, 2],
        'no_of_mobiles_purchased': [10, 3, 5, 65, 34, 6, 21, 76, 9]
    })
    print(df)
    target = 'no_of_mobiles_purchased'
    features=set(df.columns.tolist()).difference(set([target]))
    print(f'target --> {target}')
    print(f'features --> {features}')
    rw_df = relative_importance(df,
                                target=target,
                                features=features,
                                verbose=True)
    print(rw_df)