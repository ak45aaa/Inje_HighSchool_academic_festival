def paint_graph(history, title=None, ax=None, show_graph=False):
    import matplotlib.pyplot as plt
    if ax is None:
        ax = plt
        ax.plot(history.history['loss'])
        ax.plot(history.history['val_loss'])
        ax.xlabel('epochs')
        ax.ylabel('loss')
        ax.legend(['loss', 'val_loss'])
        if title is None:
            ax.title('loss graph')
        else:
            ax.title(title)
        if show_graph:
            plt.show()
    else:
        ax.plot(history.history['loss'])
        ax.plot(history.history['val_loss'])
        ax.set_xlabel('epochs')
        ax.set_ylabel('loss')
        ax.legend(['loss', 'val_loss'])
        if title is None:
            ax.set_title('loss graph')
        else:
            ax.set_title(title)
        if show_graph:
            plt.show()