import 'package:book_client/books_screen/books_screen_wm.dart';
import 'package:book_client/books_screen/widgets/book_card.dart';
import 'package:elementary/elementary.dart';
import 'package:elementary_helper/elementary_helper.dart';
import 'package:flutter/material.dart';

class BooksScreen extends ElementaryWidget<IBooksScreenWM> {
  const BooksScreen({
    Key? key,
    WidgetModelFactory wmFactory = createBooksScreenWM,
  }) : super(wmFactory, key: key);

  @override
  Widget build(IBooksScreenWM wm) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Каталог книг'),
      ),
      body: EntityStateNotifierBuilder(
        listenableEntityState: wm.booksState,
        loadingBuilder: (context, data) => const Center(
          child: CircularProgressIndicator.adaptive(),
        ),
        builder: (_, books) {
          return books == null
              ? const Center(
                  child: Text('No books:('),
                )
              : GridView(
                  gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                    crossAxisCount: 2,
                    childAspectRatio: 1 / 1.5,
                  ),
                  children: books
                      .map(
                        (book) => Padding(
                          padding: const EdgeInsets.all(5),
                          child: BookCard(book: book),
                        ),
                      )
                      .toList(),
                );
        },
      ),
    );
  }
}
