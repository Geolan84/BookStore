import 'package:book_client/books_screen/books_screen.dart';
import 'package:book_client/books_screen/books_screen_model.dart';
import 'package:book_client/domain/book.dart';
import 'package:book_client/domain/books_api_client.dart';
import 'package:dio/dio.dart';
import 'package:elementary/elementary.dart';
import 'package:elementary_helper/elementary_helper.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';

/// Factory for [BooksScreenWM].
BooksScreenWM createBooksScreenWM(BuildContext context) {
  return BooksScreenWM(
    BooksScreenModel(
      apiClient: BooksApiClient(
        dioClient: Dio(),
      ),
    ),
  );
}

class BooksScreenWM extends WidgetModel<BooksScreen, BooksScreenModel>
    implements IBooksScreenWM {
  BooksScreenWM(
    super._model,
  );

  @override
  void initWidgetModel() {
    super.initWidgetModel();
    loadBooks();
  }

  Future<void> loadBooks() async {
    _booksState.loading();
    final res = await model.loadBooks();
    _booksState.content(res);
  }

  final _booksState = EntityStateNotifier<List<Book>>();

  @override
  ValueListenable<EntityState<List<Book>>> get booksState => _booksState;
}

// Interface of [BooksScreenWM].
abstract class IBooksScreenWM implements IWidgetModel {
  ValueListenable<EntityState<List<Book>>> get booksState;
}
