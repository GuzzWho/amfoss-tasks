import 'dart:ui';
import 'package:flame/game.dart';
import 'player.dart';
import 'package:flame/components.dart';
import 'directions.dart';

class MyGame extends FlameGame {
  bunnyPlayer bunny = bunnyPlayer();
  double playerScaleFactor = 1.0;
  bool running = true;
  late Rect levelBounds;

  @override
  Future<void> onLoad() async {
    await super.onLoad();

    SpriteComponent background = SpriteComponent()
      ..sprite = await loadSprite('background.png')
      ..size = Vector2(1024.0, 720.0);

    add(background);
    levelBounds = Rect.fromLTWH(0, 0, 1024.0, 720.0);

    await add(bunny);
    bunny.position = background.size / 1.5;
    camera.followComponent(bunny, worldBounds: levelBounds);
  }

  onArrowKeyChanged(Direction direction) {
    bunny.direction = direction;
  }
}
